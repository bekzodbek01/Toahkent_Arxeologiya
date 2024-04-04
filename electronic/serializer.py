from rest_framework import serializers
from electronic.models import Electronic


class ElectronicSerializers(serializers.ModelSerializer):
    model = Electronic
    fields = ('id', 'title','book')

