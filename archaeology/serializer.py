from rest_framework import serializers
from archaeology.models import Archaeology


class ArchaeologySerializers(serializers.ModelSerializer):
    model = Archaeology
    fields = ('id', 'title', 'descriptions', 'video', 'image')
