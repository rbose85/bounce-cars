from rest_framework import serializers

from trades.models import Trade


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Regulate what goes over the wire for a `Trade` resource.
    """

    class Meta:
        model = Trade
        exclude = ("created", "modified")

    def __init__(self, *args, **kwargs):
        """custom initialisation of serializer to support dynamic field list"""
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs["context"].pop("fields", None)

        # Instantiate the superclass normally
        super(TradeSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop fields not specified in the `fields` argument.
            for field_name in (set(self.fields.keys()) - set(fields)):
                self.fields.pop(field_name)
