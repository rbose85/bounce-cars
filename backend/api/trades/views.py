from rest_framework import viewsets

from trades.models import Trade
from .serializers import TradeSerializer


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only list of `Trade` instances.
    """
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
