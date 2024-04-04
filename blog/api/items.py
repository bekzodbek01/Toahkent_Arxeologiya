from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Items
from items.serializer import ItemsSerializers


class ItemsListAPIView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers


class ItemsRetrieveAPIView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers