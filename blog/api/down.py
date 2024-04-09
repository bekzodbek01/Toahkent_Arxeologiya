from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Items


class FileDownAsarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Items.objects.get(id=pk)
        except Items.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.downloads += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.video.url)
        }
        return Response(response, status=status.HTTP_200_OK)
