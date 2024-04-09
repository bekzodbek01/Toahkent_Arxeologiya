from rest_framework.renderers import JSONRenderer  # JSONRenderer ni import qilib oling
import random

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

    def get_queryset(self):
        random_list = list(Archaeology.objects.all().order_by('?')[:2])
        random.shuffle(random_list)
        return random_list[:2]

@api_view(['GET'])
def detail_archaeology(request, pk):
    try:
        archaeology_instance = Archaeology.objects.get(pk=pk)
    except Archaeology.DoesNotExist:
        raise Http404

    archaeology_instance.view_count += 1
    archaeology_instance.save()

    serializer = ArchaeologySerializers(archaeology_instance)

    return Response({
        'data': serializer.data,})
        # 'view_count': archaeology_instance.view_count