import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_random_serializer_data, get_random_serializer_seq_data, save_character_auth_user
from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, AdditionalInfo, Catastrophe, BunkerItems, BunkerRooms, Bunker, SpecialAction
from .serializers import ProfessionSerializer, HealthSerializer, HobbySerializer, PhobiaSerializer, TraitSerializer, PhysiqueSerializer, BaggageSerializer, AdditionalInfoSerializer, CatastropheSerializer, BunkerItemsSerializer, BunkerRoomsSerializer, BunkerSerializer, SpecialActionSerializer


class GenderRandomAPIView(APIView):
    ''' Get random age, gender and fertility '''
    def get(self, request):
        gender = random.choice(['Мужчина', 'Женщина'])
        age = random.randint(18, 85)
        fertility = random.randint(0, 4)

        serializer_data = {
            'gender': gender,
            'age': age,
            'fertility': 'Чайлдфри' if fertility == 1 else 'Плодовит',
        }

        return Response(serializer_data)


class ProfessionRandomAPIView(APIView):
    ''' Get random profession '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Profession, ProfessionSerializer)

        return Response(serializer_data)


class HealthRandomAPIView(APIView):
    ''' Get random health '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Health, HealthSerializer)

        return Response(serializer_data)


class HobbyRandomAPIView(APIView):
    ''' Get random hobby '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Hobby, HobbySerializer)

        return Response(serializer_data)


class PhobiaRandomAPIView(APIView):
    ''' Get random phobia '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Phobia, PhobiaSerializer)

        return Response(serializer_data)


class TraitRandomAPIView(APIView):
    ''' Get random character trait '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Trait, TraitSerializer)

        return Response(serializer_data)


class PhysiqueRandomAPIView(APIView):
    ''' Get random physique '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Physique, PhysiqueSerializer)

        return Response(serializer_data)


class BaggageRandomAPIView(APIView):
    ''' Get random baggage '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Baggage, BaggageSerializer)

        return Response(serializer_data)


class AdditionalInfoRandomAPIView(APIView):
    ''' Get random additional information '''
    def get(self, request):
        serializer_data = get_random_serializer_data(AdditionalInfo, AdditionalInfoSerializer)

        return Response(serializer_data)


class CatastropheRandomAPIView(APIView):
    ''' Get random catastrophe '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Catastrophe, CatastropheSerializer)

        return Response(serializer_data)


class BunkerItemsRandomAPIView(APIView):
    ''' Get random bunker items '''
    def get(self, request):
        serializer_data = get_random_serializer_seq_data(BunkerItems, BunkerItemsSerializer)

        return Response(serializer_data)
    

class BunkerRoomsRandomAPIView(APIView):
    ''' Get random bunker rooms '''
    def get(self, request):
        serializer_data = get_random_serializer_seq_data(BunkerRooms, BunkerRoomsSerializer)

        return Response(serializer_data)
    

class BunkerRandomAPIView(APIView):
    ''' Get random bunker '''
    def get(self, request):
        serializer_data = get_random_serializer_data(Bunker, BunkerSerializer)

        return Response(serializer_data)
    

class CharacterGenerateAPIView(APIView):
    ''' Generate character '''
    def get(self, request):
        gender = random.choice(['Мужчина', 'Женщина'])
        age = random.randint(18, 85)
        fertility = random.randint(0, 4)

        profession = get_random_serializer_data(Profession, ProfessionSerializer)
        health = get_random_serializer_data(Health, HealthSerializer)
        physique = get_random_serializer_data(Physique, PhysiqueSerializer)
        trait = get_random_serializer_data(Trait, TraitSerializer)
        hobby = get_random_serializer_data(Hobby, HobbySerializer)
        phobia = get_random_serializer_data(Phobia, PhobiaSerializer)
        baggage = get_random_serializer_data(Baggage, BaggageSerializer)
        additional_info = get_random_serializer_data(AdditionalInfo, AdditionalInfoSerializer)
        special_action_one = get_random_serializer_data(SpecialAction, SpecialActionSerializer)
        special_action_two = get_random_serializer_data(SpecialAction, SpecialActionSerializer)

        serializer_data = {
            'gender': gender,
            'age': age,
            'fertility': 'Чайлдфри' if fertility == 1 else 'Плодовит',
            'profession': profession,
            'health': health,
            'physique': physique,
            'trait': trait,
            'hobby': hobby,
            'phobia': phobia,
            'baggage': baggage,
            'additional_info': additional_info,
            'special_action_one': special_action_one,
            'special_action_two': special_action_two,
        }

        save_character_auth_user(serializer_data)

        return Response(serializer_data)