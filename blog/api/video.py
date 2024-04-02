from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Video
from blog.serializer import VideoSerializers


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class VideoRetrieveAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
