import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Proffesion, HealthStatus, Hobbies, Phobia, CharacterTrait, Physique, Items, AdditionalInfo
from .serializers import ProffesionSerializer, HealthStatusSerializer, HobbiesSerializer, PhobiaSerializer, CharacterTraitSerializer, PhysiqueSerializer, ItemsSerializer, AdditionalInfoSerializer


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


class ProffesionRandomAPIView(APIView):
    ''' Get random profession '''
    def get(self, request):
        random_proffesion = Proffesion.objects.order_by('?').first()
        serializer_data = ProffesionSerializer(random_proffesion).data

        return Response(serializer_data)


class HealthRandomAPIView(APIView):
    ''' Get random health '''
    def get(self, request):
        random_health = HealthStatus.objects.order_by('?').first()
        serializer_data = HealthStatusSerializer(random_health).data

        return Response(serializer_data)


class HobbyRandomAPIView(APIView):
    ''' Get random hobby '''
    def get(self, request):
        random_hobby = Hobbies.objects.order_by('?').first()
        serializer_data = HobbiesSerializer(random_hobby).data

        return Response(serializer_data)


class PhobiaRandomAPIView(APIView):
    ''' Get random phobia '''
    def get(self, request):
        random_phobia = Phobia.objects.order_by('?').first()
        serializer_data = PhobiaSerializer(random_phobia).data

        return Response(serializer_data)


class TraitRandomAPIView(APIView):
    ''' Get random character trait '''
    def get(self, request):
        random_trait = CharacterTrait.objects.order_by('?').first()
        serializer_data = CharacterTraitSerializer(random_trait).data

        return Response(serializer_data)


class PhysiqueRandomAPIView(APIView):
    ''' Get random physique '''
    def get(self, request):
        random_physique = Physique.objects.order_by('?').first()
        serializer_data = PhysiqueSerializer(random_physique).data

        return Response(serializer_data)


class BaggageRandomAPIView(APIView):
    ''' Get random baggage '''
    def get(self, request):
        random_baggage = Items.objects.order_by('?').first()
        serializer_data = ItemsSerializer(random_baggage).data

        return Response(serializer_data)


class InfoRandomAPIView(APIView):
    ''' Get random additional information '''
    def get(self, request):
        random_info = AdditionalInfo.objects.order_by('?').first()
        serializer_data = AdditionalInfoSerializer(random_info).data

        return Response(serializer_data)