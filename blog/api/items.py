from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from items.models import Items
from items.serializer import ItemsSerializers
from blog.pagination import ResultsSetPagination


class ItemsListAPIView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers
    paginator_class = ResultsSetPagination


@api_view(['GET'])
def items_detail(request, pk):
    try:
        new = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        raise Http404

    serializer = ItemsSerializers(new)
    return Response(serializer.data)
