from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News
from news.serializer import NewsSerializers


@api_view(['GET'])
def list_news(request):
    news = News.objects.all().order_by("id")
    serializer = NewsSerializers(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, pk):
    try:
        new = News.objects.get(pk=pk)
    except News.DoesNotExist:
        raise Http404

    serializer = NewsSerializers(new)
    return Response(serializer.data)
