from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from video.models import Video
from video.serializer import VideoSerializers



@api_view(['GET'])
def list_video(request):
    video = Video.objects.all().order_by("id")
    serializer = VideoSerializers(video, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def video_detail(request, pk):
    try:
        vid = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        raise Http404

    serializer = VideoSerializers(vid)
    return Response(serializer.data)


