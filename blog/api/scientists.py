from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import Scientists
from blog.serializer import ScientistSerializers


class ScientistsListAPIView(ListAPIView):
    queryset = Scientists.objects.all()
    serializer_class = ScientistSerializers


class ScientistsRetrieveAPIView(RetrieveAPIView):
    queryset = Scientists.objects.all()
    serializer_class = ScientistSerializers
