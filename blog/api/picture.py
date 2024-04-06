from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from picture.models import Picture
from picture.serializer import PictureSerializers



@api_view(['GET'])
def list_picture(request):
    pictur = Picture.objects.all().order_by("id")
    serializer = PictureSerializers(pictur, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def picture_detail(request, pk):
    try:
        picture = Picture.objects.get(pk=pk)
    except Picture.DoesNotExist:
        raise Http404

    serializer = PictureSerializers(picture)
    return Response(serializer.data)
