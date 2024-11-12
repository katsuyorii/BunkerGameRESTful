from rest_framework import serializers

from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, SpecialAction, AdditionalInfo


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['name',]


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = ['name',]


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['name',]


class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phobia
        fields = ['name',]


class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ['name',]


class PhysiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physique
        fields = ['name',]


class BaggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baggage
        fields = ['name',]


class SpecialActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialAction
        fields = ['description',]


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['description',]