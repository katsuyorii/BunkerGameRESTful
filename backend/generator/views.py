import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_random_serializer_data, get_random_serializer_seq_data
from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, AdditionalInfo, Catastrophe, BunkerItems, BunkerRooms
from .serializers import ProfessionSerializer, HealthSerializer, HobbySerializer, PhobiaSerializer, TraitSerializer, PhysiqueSerializer, BaggageSerializer, AdditionalInfoSerializer, CatastropheSerializer, BunkerItemsSerializer, BunkerRoomsSerializer


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