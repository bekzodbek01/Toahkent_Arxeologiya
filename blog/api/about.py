from rest_framework.generics import ListAPIView,RetrieveAPIView
from about.models import About
from about.serializer import AboutSerializers


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers


class AboutRetrieveAPIView(RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializers

