'''Defines the serializers for metrics'''
from __future__ import unicode_literals

import rest_framework.pagination as pagination
import rest_framework.serializers as serializers


class MetricsTypeBaseSerializer(serializers.Serializer):
    '''Converts metrics type model fields to REST output'''
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()


class MetricsTypeFilterSerializer(serializers.Serializer):
    '''Converts metrics filter model fields to REST output'''
    param = serializers.CharField()
    type = serializers.CharField()


class MetricsTypeColumnSerializer(serializers.Serializer):
    '''Converts metrics column model fields to REST output'''
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    units = serializers.CharField()
    group = serializers.CharField()
    aggregate = serializers.CharField()


class MetricsTypeGroupSerializer(serializers.Serializer):
    '''Converts metrics group model fields to REST output'''
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()


class MetricsTypeSerializer(serializers.Serializer):
    '''Converts metrics type model fields to REST output'''
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    filters = MetricsTypeFilterSerializer()
    groups = MetricsTypeGroupSerializer()
    columns = MetricsTypeColumnSerializer()


class MetricsTypeListSerializer(pagination.PaginationSerializer):
    '''Converts a list of metrics type models to paginated REST output'''

    class Meta(object):
        '''meta information for the serializer'''
        object_serializer_class = MetricsTypeSerializer


class MetricsTypeDetailsSerializer(MetricsTypeSerializer):
    '''Converts metrics details model fields to REST output'''
    choices = serializers.CharField()


class MetricsPlotValueSerializer(serializers.Serializer):
    '''Converts metrics plot values to REST output'''
    date = serializers.DateField()
    value = serializers.IntegerField()


class MetricsPlotMultiValueSerializer(MetricsPlotValueSerializer):
    '''Converts metrics plot values to REST output'''
    id = serializers.IntegerField()


class MetricsPlotSerializer(serializers.Serializer):
    '''Converts metrics plot values to REST output'''
    column = MetricsTypeColumnSerializer()
    min_x = serializers.IntegerField()
    max_x = serializers.IntegerField()
    min_y = serializers.IntegerField()
    max_y = serializers.IntegerField()
    values = MetricsPlotValueSerializer()


class MetricsPlotMultiSerializer(MetricsPlotSerializer):
    '''Converts metrics plot values to REST output'''
    values = MetricsPlotMultiValueSerializer()


class MetricsPlotListSerializer(pagination.PaginationSerializer):
    '''Converts a list of metrics plot models to paginated REST output'''

    class Meta(object):
        '''meta information for the serializer'''
        object_serializer_class = MetricsPlotSerializer


class MetricsPlotMultiListSerializer(pagination.PaginationSerializer):
    '''Converts a list of metrics plot models to paginated REST output'''

    class Meta(object):
        '''meta information for the serializer'''
        object_serializer_class = MetricsPlotMultiSerializer


class MetricsIngestDetailsSerializer(MetricsTypeDetailsSerializer):
    '''Converts ingest metrics details model fields to REST output'''
    from ingest.serializers import StrikeBaseSerializer

    choices = StrikeBaseSerializer()


class MetricsJobTypeDetailsSerializer(MetricsTypeDetailsSerializer):
    '''Converts job type metrics details model fields to REST output'''
    from job.serializers import JobTypeBaseSerializer

    choices = JobTypeBaseSerializer()
