from datetime import datetime

from django.core.exceptions import ValidationError
from djangorestframework_camel_case.util import camel_to_underscore
from rest_framework import serializers, viewsets

from trades.models import Trade
from .serializers import TradeSerializer


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only list of `Trade` instances.
    """
    model = Trade
    serializer_class = TradeSerializer

    @staticmethod
    def __iso_string_to_datetime(iso_string):
        """build datetime obj from iso8601 string"""
        try:
            dt = serializers.DateTimeField().from_native(iso_string)
        except ValidationError:
            return None
        return dt

    def __reduce_serializer_field_set(self, field_names):
        """iterate over list of field names and return preferred super-set"""
        default_fields = list(self.get_serializer_class()().get_fields().keys())
        for fn in field_names:
            if fn not in default_fields:
                return None
        return field_names

    def __extract_from_querystring(self, param_name, param_cls):
        """search querystring for parameter by name and return as instance"""
        param = self.request.QUERY_PARAMS.get(param_name)
        if param is None:
            return param

        if param_cls.__name__ == 'datetime':
            return self.__iso_string_to_datetime(iso_string=param)

        if param_cls.__name__ == 'list':
            underscored = [camel_to_underscore(x) for x in param.split(',')]
            return self.__reduce_serializer_field_set(field_names=underscored)

        return None

    def get_queryset(self):
        """Optionally reduce the complete dataset by url query parameters."""
        queryset = Trade.objects.all()

        start = self.__extract_from_querystring('timestamp_begin', datetime)
        if start is not None:
            queryset = queryset.filter(time_stamp__gt=start)

        finish = self.__extract_from_querystring('timestamp_end', datetime)
        if finish is not None:
            queryset = queryset.filter(time_stamp__lte=finish)

        return queryset

    def get_serializer_context(self):
        """Optionally set queryset fields based on url query parameters."""
        context = super(TradeViewSet, self).get_serializer_context()

        preferreds = self.__extract_from_querystring('preferred_columns', list)
        context['fields'] = preferreds
        return context
