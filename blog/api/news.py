from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News
from rest_framework.generics import ListAPIView
from news.serializer import NewsSerializers
from blog.pagination import ResultsSetPagination



class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    paginator_class = ResultsSetPagination



@api_view(['GET'])
def news_detail(request, pk):
    try:
        new = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsSerializers(new)
    return Response(serializer.data)
