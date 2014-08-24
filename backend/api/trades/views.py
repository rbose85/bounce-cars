from datetime import datetime

from django.core.exceptions import ValidationError
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
        """iterate over list of strings and build datetime obj from each iso"""
        try:
            dt = serializers.DateTimeField().from_native(iso_string)
        except ValidationError:
            return None
        return dt

    def __extract_from_querystring(self, param_name, param_cls):
        """search querystring for parameter by name and return as instance"""
        param = self.request.QUERY_PARAMS.get(param_name)
        if param is None:
            return None
        if param_cls.__name__ == 'datetime':
            return self.__iso_string_to_datetime(iso_string=param)
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
