from rest_framework import serializers
from electronic.models import Electronic


class ElectronicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = ('id', 'title','book')

