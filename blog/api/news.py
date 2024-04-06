from rest_framework.generics import ListAPIView, RetrieveAPIView
from news.models import News
from news.serializer import NewsSerializers
from blog.pagination import ResultsSetPagination


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    paginator_class = ResultsSetPagination

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers