'''Defines the ingest trigger rule'''
from __future__ import unicode_literals

import logging

from django.db import transaction
from django.db.models import Q

from ingest.triggers.ingest_event import TRIGGER_TYPE, IngestTriggerEvent
from job.configuration.data.job_data import JobData
from job.models import JobType
from queue.models import Queue
from recipe.configuration.data.recipe_data import RecipeData
from recipe.models import RecipeType
from storage.models import Workspace
from trigger.exceptions import InvalidTriggerRule
from trigger.models import TriggerRule


logger = logging.getLogger(__name__)


DEFAULT_VERSION = '1.0'


def get_ingest_rules():
    '''Retrieves the ingest trigger rules from the database

    :returns: List of the ingest trigger rules
    :rtype: list of :class:`ingest.triggers.IngestTriggerRule`
    '''

    rule_list = []
    for rule_model in TriggerRule.objects.get_active_trigger_rules(TRIGGER_TYPE):
        rule = IngestTriggerRule(rule_model.configuration, rule_model)
        rule_list.append(rule)

    return rule_list


class IngestTriggerRule(object):
    '''Represents a rule that is triggered when a source file is ingested
    '''

    def __init__(self, configuration, model=None):
        '''Creates an ingest trigger rule from the given dictionary. The general format is checked for correctness, but
        the actual ingested file details are not checked for correctness against the interface of any jobs that should
        be created when triggered. If the general format is invalid, a :class:`trigger.exceptions.InvalidTriggerRule`
        will be thrown.

        :param configuration: The job data
        :type configuration: dict
        :param model: The trigger rule model
        :type model: :class:`trigger.models.TriggerRule`
        '''

        if 'version' not in configuration:
            configuration['version'] = DEFAULT_VERSION
        if not configuration['version'] == '1.0':
            raise InvalidTriggerRule('%s is an unsupported version number' % configuration['version'])

        if 'trigger' not in configuration:
            configuration['trigger'] = {}
        if 'media_type' not in configuration['trigger']:
            configuration['trigger']['media_type'] = ''
        media_type = configuration['trigger']['media_type']
        if not isinstance(media_type, basestring):
            raise InvalidTriggerRule('Rule must have a string in its "media_type" field')

        if 'data_types' not in configuration['trigger']:
            configuration['trigger']['data_types'] = []
        data_types_list = configuration['trigger']['data_types']
        if not isinstance(data_types_list, list):
            raise InvalidTriggerRule('trigger->data_types must be empty or an array')
        for data_type in data_types_list:
            if not isinstance(data_type, basestring):
                raise InvalidTriggerRule('Rule may only have strings in its "data_types" field')

        if 'create' not in configuration:
            configuration['create'] = {}
        if 'jobs' not in configuration['create']:
            configuration['create']['jobs'] = []
        for job in configuration['create'].get('jobs', []):
            if 'job_type' not in job:
                raise InvalidTriggerRule('Every job must have a "job_type" field')
            job_type = job['job_type']

            if 'name' not in job_type:
                raise InvalidTriggerRule('Every job type must have a "name" field')
            job_name = job_type['name']
            if not isinstance(job_name, basestring):
                raise InvalidTriggerRule('Every job must have a string in its "name" field')

            if 'version' not in job_type:
                raise InvalidTriggerRule('Every job type must have a "version" field')
            job_version = job_type['version']
            if not isinstance(job_version, basestring):
                raise InvalidTriggerRule('Every job must have a string in its "version" field')

            if 'file_input_name' not in job:
                raise InvalidTriggerRule('Every job must have a "file_input_name" field')
            file_input_name = job['file_input_name']
            if not isinstance(file_input_name, basestring):
                raise InvalidTriggerRule('Every job must have a string in its "file_input_name" field')

            if 'workspace_name' in job:
                workspace_name = job['workspace_name']
                if not isinstance(workspace_name, basestring):
                    raise InvalidTriggerRule('Every job must have a string in its "workspace_name" field')

        for recipe in configuration['create'].get('recipes', []):
            if 'recipe_type' not in recipe:
                raise InvalidTriggerRule('Every recipe must have a "recipe_type" field')
            recipe_type = recipe['recipe_type']

            if 'name' not in recipe_type:
                raise InvalidTriggerRule('Every recipe type must have a "name" field')
            recipe_name = recipe_type['name']
            if not isinstance(recipe_name, basestring):
                raise InvalidTriggerRule('Every recipe type must have a string in its "name" field')

            if 'version' not in recipe_type:
                raise InvalidTriggerRule('Every recipe type must have a "version" field')
            recipe_version = recipe_type['version']
            if not isinstance(recipe_version, basestring):
                raise InvalidTriggerRule('Every recipe type must have a string in its "version" field')

            if 'file_input_name' not in recipe:
                raise InvalidTriggerRule('Every recipe must have a "file_input_name" field')
            file_input_name = recipe['file_input_name']
            if not isinstance(file_input_name, basestring):
                raise InvalidTriggerRule('Every recipe must have a string in its "file_input_name" field')

            if 'workspace_name' in recipe:
                workspace_name = recipe['workspace_name']
                if not isinstance(workspace_name, basestring):
                    raise InvalidTriggerRule('Every recipe must have a string in its "workspace_name" field')

        self._configuration = configuration
        self._model = model
        self._media_type = self._configuration['trigger']['media_type']
        self._data_types = set(data_types_list) if data_types_list else set()
        self._jobs_to_create = self._configuration['create']['jobs']
        self._recipes_to_create = self._configuration['create'].get('recipes', [])

        # Build a mapping of referenced job type models
        job_configs = [job['job_type'] for job in self._jobs_to_create]
        self._job_type_map = self._get_type_map(JobType, job_configs)

        # Build a mapping of referenced recipe type models
        recipe_configs = [recipe['recipe_type'] for recipe in self._recipes_to_create]
        self._recipe_type_map = self._get_type_map(RecipeType, recipe_configs)

        # Build a mapping of referenced workspace models
        workspace_configs = []
        workspace_configs.extend(self._jobs_to_create)
        workspace_configs.extend(self._recipes_to_create)
        self._workspace_map = self._get_workspace_map(workspace_configs)

    @transaction.atomic
    def process_ingest(self, ingest, source_file_id):
        '''Processes the given source file ingest by creating the appropriate jobs if the rule is triggered. All
        database changes are made in an atomic transaction.

        :param ingest: The ingest to process
        :type ingest: :class:`ingest.models.Ingest`
        :param source_file_id: The ID of the source file that was ingested
        :type source_file_id: long
        '''

        # Only trigger when this ingest file has the correct media type and ingest types
        if self._media_type and self._media_type != ingest.media_type:
            return
        if not self._data_types.issubset(ingest.get_data_type_tags()):
            return

        if not self._media_type:
            logger.info('Ingest rule for all media types was triggered')
        else:
            logger.info('Ingest rule for media type %s was triggered', self._media_type)
        event = IngestTriggerEvent(self._model, ingest).save_to_db()

        # Create triggered jobs
        for job in self._jobs_to_create:
            job_type = self._job_type_map[(job['job_type']['name'], job['job_type']['version'])]
            file_input_name = job['file_input_name']
            job_data = JobData({})
            job_data.add_file_input(file_input_name, source_file_id)

            # If workspace name has been provided, add that to the job data for each output file
            if 'workspace_name' in job:
                workspace = self._workspace_map[job['workspace_name']]
                job_type.get_job_interface().add_workspace_to_data(job_data, workspace.id)
            logger.info('Queuing new job of type %s %s', job_type.name, job_type.version)
            Queue.objects.queue_new_job(job_type, job_data.get_dict(), event)

        # Create triggered recipes
        for recipe in self._recipes_to_create:
            recipe_type = self._recipe_type_map[(recipe['recipe_type']['name'], recipe['recipe_type']['version'])]
            file_input_name = recipe['file_input_name']
            recipe_data = RecipeData({})
            recipe_data.add_file_input(file_input_name, source_file_id)

            # If workspace name has been provided, add that to the recipe data for each output file
            if 'workspace_name' in recipe:
                workspace = self._workspace_map[recipe['workspace_name']]
                recipe_data.set_workspace_id(workspace.id)
            logger.info('Queuing new recipe of type %s %s', recipe_type.name, recipe_type.version)
            Queue.objects.queue_new_recipe(recipe_type, recipe_data.get_dict(), event)

    def save_to_db(self):
        '''Saves the ingest trigger rule to the database

        :returns: The new trigger rule model
        :rtype: :class:`trigger.models.TriggerRule`
        '''

        if self._model:
            raise Exception('Rule is already saved in the database')

        self._model = TriggerRule.objects.create_trigger_rule(TRIGGER_TYPE, self._configuration)
        return self._model

    def validate(self):
        '''Validates the ingest trigger rule to ensure that it will be able to successfully queue its configured jobs
        when triggered. If the job configuration is invalid, a :class:`trigger.exceptions.InvalidTriggerRule` or
        :class:`job.configuration.data.exceptions.InvalidData` will be thrown.
        '''

        # TODO: implement
        # NOTE: this should be called by the future RESTful API that creates ingest trigger rules
        pass

    def _get_type_map(self, model_class, configuration):
        '''Builds a mapping for a model type and configuration of natural key to model instance.

        This is a shared method to fetch JobType and RecipeType declarations.

        :param model_class: A class reference to the type of model to map.
        :type model_class: :class:`django.models.Model`
        :param configuration: A list of configurations that specify natural keys of models to fetch and map.
        :type configuration: list[dict]
        :returns: A mapping of natural keys to associated model instances. The natural keys consist of a two-element
            tuple with a name and version field.
        :rtype: dict[(string, string), :class:`django.models.Model`]
        '''

        # Build a mapping of required types
        results = dict()
        query = None
        for config in configuration:
            name = config['name']
            version = config['version']
            tuple_key = (name, version)

            # Create a query filter for each type
            if tuple_key not in results:
                results[tuple_key] = None
                query_filter = Q(name=name, version=version)
                query = query | query_filter if query else query_filter

        # Fetch each type model and map it
        if query:
            for model_type in model_class.objects.filter(query):
                results[(model_type.name, model_type.version)] = model_type

        # Check for any missing model type declarations
        for tuple_key, model_type in results.iteritems():
            if not model_type:
                name, version = tuple_key
                raise InvalidTriggerRule('Unknown type reference: %s(%s, %s)' % (model_class, name, version))

        return results

    def _get_workspace_map(self, configuration):
        '''Builds a mapping for a workspace and configuration of name to model instance.

        :param configuration: A list of configurations that specify system names of models to fetch and map.
        :type configuration: list[dict]
        :returns: A mapping of workspace system names to associated model instances.
        :rtype: dict[string, :class:`storage.models.Workspace`]
        '''

        # Build a mapping of required workspaces
        results = dict()
        query = None
        for config in configuration:
            if not 'workspace_name' in config:
                continue
            name = config['workspace_name']

            # Create a query filter for each workspace
            if name not in results:
                results[name] = None
                query_filter = Q(name=name)
                query = query | query_filter if query else query_filter

        # Fetch each workspace model and map it
        if query:
            for workspace in Workspace.objects.filter(query):
                results[workspace.name] = workspace

        # Check for any missing workspace model declarations
        for name, workspace in results.iteritems():
            if not workspace:
                raise InvalidTriggerRule('Unknown workspace reference: %s' % name)

        return results
