from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from electronic.models import Electronic
from electronic.serializer import ElectronicSerializers


@api_view(['GET'])
def list_electronic(request):
    news = Electronic.objects.all().order_by("id")
    serializer = ElectronicSerializers(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def electronic_detail(request, pk):
    try:
        new = Electronic.objects.get(pk=pk)
    except Electronic.DoesNotExist:
        raise Http404

    serializer = ElectronicSerializers(new)
    return Response(serializer.data)
