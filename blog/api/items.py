from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Items
from items.serializer import ItemsSerializers
from blog.pagination import ResultsSetPagination

class ItemsListAPIView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers
    paginator_class = ResultsSetPagination


class ItemsRetrieveAPIView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers