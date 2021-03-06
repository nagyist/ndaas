'''The scale ingest application'''
from __future__ import unicode_literals

from django.apps import AppConfig


class IngestConfig(AppConfig):
    '''Configuration for the ingest app
    '''
    name = 'ingest'
    label = 'ingest'
    verbose_name = 'Ingest'

    def ready(self):
        """
        Override this method in subclasses to run code when Django starts.
        """

        from ingest.cleanup import IngestJobExecutionCleaner
        from ingest.strike.cleanup import StrikeJobExecutionCleaner
        from job.execution.cleanup import REGISTERED_CLEANERS

        # Register job execution cleaners for ingest and Strike jobs
        REGISTERED_CLEANERS['scale-ingest'] = IngestJobExecutionCleaner()
        REGISTERED_CLEANERS['scale-strike'] = StrikeJobExecutionCleaner()
