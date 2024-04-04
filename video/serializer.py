from rest_framework import serializers
from video.models import Video


class VideoSerializers(serializers.ModelSerializer):
    model = Video
    fields = ('id', 'title','video')
