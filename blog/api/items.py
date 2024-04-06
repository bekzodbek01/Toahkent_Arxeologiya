from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from items.models import Items
from items.serializer import ItemsSerializers


@api_view(['GET'])
def list_items(request):
    news = Items.objects.all().order_by("id")
    serializer = ItemsSerializers(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def items_detail(request, pk):
    try:
        new = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        raise Http404

    serializer = ItemsSerializers(new)
    return Response(serializer.data)
