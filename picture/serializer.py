from rest_framework import serializers
from picture.models import Picture


class PictureSerializers(serializers.ModelSerializer):
    model = Picture
    fields = ('id', 'title','image')

