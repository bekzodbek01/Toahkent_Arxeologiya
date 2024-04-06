
from archaeology.models import Archaeology
from archaeology.serializer import ArchaeologySerializers
from blog.pagination import ResultsSetPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.generics import ListAPIView



class ArchaeologyListAPIView(ListAPIView):
    queryset = Archaeology.objects.all()
    serializer_class = ArchaeologySerializers
    paginator_class = ResultsSetPagination


# Detail
@api_view(['GET'])
def detail_archaeology(request,pk):
    try:
        about = Archaeology.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        raise Http404

    serializer = ArchaeologySerializers(about)
    return Response(serializer.data)






