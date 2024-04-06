
from about.models import About
from about.serializer import AboutSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404


# Read (O'qish)
@api_view(['POST'])
def list_about(request):
    about = About.objects.all().order_by('id')
    serializer = AboutSerializers(about,many=True)
    return Response(serializer.data)


# Detail
@api_view(['POST'])
def detail_about(request,pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        raise Http404

    serializer = AboutSerializers(about)
    return Response(serializer.data)

