import random

from rest_framework import serializers

from .services import get_random_serializer_seq_data
from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, SpecialAction, AdditionalInfo, Catastrophe, BunkerItems, BunkerRooms, Bunker


class ProfessionSerializer(serializers.ModelSerializer):
    exp = serializers.SerializerMethodField()

    class Meta:
        model = Profession
        fields = ['name', 'exp',]
    
    # Method to generate random value for exp field
    def get_exp(self, obj):
        return random.randint(1, 20)


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
        model = BunkerRooms
        fields = ['name',]


class BunkerSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    rooms = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    sup_food_month = serializers.SerializerMethodField()

    class Meta:
        model = Bunker
        fields = ['title', 'description', 'items', 'rooms', 'area', 'sup_food_month',]
    
    # Method to get random values for items field
    def get_items(self, obj):
        return get_random_serializer_seq_data(BunkerItems, BunkerItemsSerializer)
    
    # Method to get random values for rooms field
    def get_rooms(self, obj):
        return get_random_serializer_seq_data(BunkerRooms, BunkerRoomsSerializer)
    
    # Method to generate random value for area field
    def get_area(self, obj):
        return random.randint(45, 150)
    
    # Method to generate random value for sup_food_month field
    def get_sup_food_month(self, obj):
        return random.randint(1, 12)