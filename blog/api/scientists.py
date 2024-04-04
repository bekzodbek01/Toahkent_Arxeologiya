from rest_framework.generics import ListAPIView, RetrieveAPIView
from scientists.models import Scientists
from scientists.serializer import ScientistSerializers


class ScientistsListAPIView(ListAPIView):
    queryset = Scientists.objects.all()
    serializer_class = ScientistSerializers


class ScientistsRetrieveAPIView(RetrieveAPIView):
    queryset = Scientists.objects.all()
    serializer_class = ScientistSerializers
