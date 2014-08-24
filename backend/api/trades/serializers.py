from rest_framework import serializers

from trades.models import Trade


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Regulate what goes over the wire for a `Trade` resource.
    """

    class Meta:
        model = Trade
        exclude = ("created", "modified")
