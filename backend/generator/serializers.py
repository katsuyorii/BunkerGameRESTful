from rest_framework import serializers

from .models import Proffesion


class ProffesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesion
        fields = ['name',]