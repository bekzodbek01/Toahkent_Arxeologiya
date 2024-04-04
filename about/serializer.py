from rest_framework import serializers
from about.models import About


class AboutSerializers(serializers.ModelSerializer):
    model = About
    fields = ('id', 'descriptions', 'video')
