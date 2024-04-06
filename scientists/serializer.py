from rest_framework import serializers
from scientists.models import Scientists


class ScientistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = ('id', 'fullname', 'position', 'descriptions', 'image')

        # def get_jadid_fullname(self, obj):
        #     return obj.jadid.fullname if obj.jadid else None
        #
        # def to_representation(self, instance):
        #     data = super().to_representation(instance)
        #     images = instance.images.all()
        #
        #     if images:
        #         request = self.context.get('request')
        #         if request:
        #             data['images'] = [{'file': request.build_absolute_uri(img.file.url)} for img in images]
        #         else:
        #             data['images'] = [{'file': img.file.url} for img in images]
        #
        #     return data
