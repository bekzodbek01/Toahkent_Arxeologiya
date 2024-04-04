from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    model = Contact
    fields = ('id', 'full_name', 'email', 'description')

