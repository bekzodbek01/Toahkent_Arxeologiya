from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Electronic
from blog.serializer import ElectronicSerializers


class ElectronicListAPIView(ListAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializers


class ElectronicRetrieveAPIView(RetrieveAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializers