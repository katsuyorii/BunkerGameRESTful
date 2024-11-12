import random

from rest_framework import serializers

from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, SpecialAction, AdditionalInfo, Catastrophe, BunkerItems, BunkerRooms


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


class CatastropheSerializer(serializers.ModelSerializer):
    perc_destruction = serializers.SerializerMethodField()
    perc_survivors = serializers.SerializerMethodField()

    class Meta:
        model = Catastrophe
        fields = ['title', 'description', 'perc_destruction', 'perc_survivors',]
    
    # Method to generate random value for perc_destruction field
    def get_perc_destruction(self, obj):
        return random.randint(60, 99)

    # Method to generate random value for perc_survivors field
    def get_perc_survivors(self, obj):
        return random.randint(0, 50)


class BunkerItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BunkerItems
        fields = ['name',]


class BunkerRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BunkerItems
        fields = ['name',]