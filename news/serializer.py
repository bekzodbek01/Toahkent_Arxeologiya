from rest_framework import serializers
from news.models import News


class NewsSerializers(serializers.ModelSerializer):
    model = News
    fields = ('id', 'title','descriptions','image')

