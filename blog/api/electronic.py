from rest_framework.generics import ListAPIView, RetrieveAPIView

from electronic.models import Electronic
from electronic.serializer import ElectronicSerializers


class ElectronicListAPIView(ListAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializers


class ElectronicRetrieveAPIView(RetrieveAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializers