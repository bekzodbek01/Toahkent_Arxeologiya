from rest_framework import serializers
from scientists.models import Scientists


class ScientistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = ('id', 'fullname', 'position','descriptions','image')
