from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import News
from blog.serializer import NewsSerializers


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers