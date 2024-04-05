from rest_framework import serializers
from picture.models import Picture


class PictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'title','image')

