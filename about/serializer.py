from rest_framework import serializers
from about.models import About


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'descriptions', 'video')

