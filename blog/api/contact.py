from rest_framework import status
from rest_framework.response import Response

from contact.models import Contact
from contact.serializer import ContactSerializer
from rest_framework.views import APIView


class ContactListCreateView(APIView):
    def get(self, request):
        news = Contact.objects.all()
        serializers = ContactSerializer(news, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = ContactSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
