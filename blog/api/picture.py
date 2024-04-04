from rest_framework.generics import ListAPIView, RetrieveAPIView
from picture.models import Picture
from picture.serializer import PictureSerializers


class PictureListAPIView(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializers


class PictureRetrieveAPIView(RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializers
