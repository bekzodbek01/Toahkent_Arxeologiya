from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Picture
from blog.serializer import PictureSerializers


class PictureListAPIView(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializers


class PictureRetrieveAPIView(RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializers
