from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scientists.models import Scientists
from scientists.serializer import ScientistSerializers


@api_view(['GET'])
def list_scientists(request):
    olimlar = Scientists.objects.all().order_by("id")
    serializer = ScientistSerializers(olimlar, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scientists_detail(request, pk):
    try:
        olim = Scientists.objects.get(pk=pk)
    except Scientists.DoesNotExist:
        raise Http404

    serializer = ScientistSerializers(olim)
    return Response(serializer.data)

