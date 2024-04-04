from rest_framework.generics import ListAPIView, RetrieveAPIView
from news.models import News
from news.serializer import NewsSerializers


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers