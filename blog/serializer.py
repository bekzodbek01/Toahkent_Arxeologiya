from rest_framework import serializers
from blog.models import About,Archaeology,Items,Scientists,Video, Picture,News, Electronic

class AboutSerializers(serializers.ModelSerializer):
    model = About
    fields = ('id','descriptions','video')


class ArchaeologySerializers(serializers.ModelSerializer):
    model = Archaeology
    fields = ('id', 'title','descriptions', 'video','image')


class ItemsSerializers(serializers.ModelSerializer):
    model = Items
    fields = ('id', 'title', 'descriptions', 'video', 'image')


class ScientistSerializers(serializers.ModelSerializer):
    model = Scientists
    fields = ('id', 'fullname', 'position','descriptions','image')


class VideoSerializers(serializers.ModelSerializer):
    model = Video
    fields = ('id', 'title','video')



class PictureSerializers(serializers.ModelSerializer):
    model = Picture
    fields = ('id', 'title','image')


class NewsSerializers(serializers.ModelSerializer):
    model = News
    fields = ('id', 'title','descriptions','image')


class ElectronicSerializers(serializers.ModelSerializer):
    model = Electronic
    fields = ('id', 'title','book')




