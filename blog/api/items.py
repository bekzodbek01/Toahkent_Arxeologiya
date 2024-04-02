from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Items
from blog.serializer import ItemsSerializers


class ItemsListAPIView(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers


class ItemsRetrieveAPIView(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializers