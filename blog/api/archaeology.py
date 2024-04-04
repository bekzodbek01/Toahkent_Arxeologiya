from rest_framework import generics, filters
from rest_framework.generics import RetrieveAPIView
from archaeology.models import Archaeology
from archaeology.serializer import ArchaeologySerializers
from blog.pagination import ResultsSetPagination


class ArchaeologyListViews(generics.ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ArchaeologySerializers
    paginator_class = ResultsSetPagination

    def get_queryset(self):
        return Archaeology.objects.all()


class ArchaeologyRetrieveAPIView(RetrieveAPIView):
    queryset = Archaeology.objects.all()
    serializer_class = ArchaeologySerializers