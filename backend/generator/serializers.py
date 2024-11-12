from rest_framework import serializers

from .models import Proffesion, HealthStatus, Hobbies, Phobia, CharacterTrait, Physique, Items, SpecialAction, AdditionalInfo


class ProffesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proffesion
        fields = ['name',]


class HealthStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthStatus
        fields = ['name',]


class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ['name',]


class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields = ['name',]


class CharacterTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterTrait
        fields = ['name',]


class PhysiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physique
        fields = ['name',]


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name',]


class SpecialActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialAction
        fields = ['description',]


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['description',]