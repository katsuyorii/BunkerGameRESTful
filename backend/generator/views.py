import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profession, Health, Hobby, Phobia, Trait, Physique, Baggage, AdditionalInfo
from .serializers import ProfessionSerializer, HealthSerializer, HobbySerializer, PhobiaSerializer, TraitSerializer, PhysiqueSerializer, BaggageSerializer, AdditionalInfoSerializer


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
        random_proffesion = Profession.objects.order_by('?').first()
        serializer_data = ProfessionSerializer(random_proffesion).data

        return Response(serializer_data)


class HealthRandomAPIView(APIView):
    ''' Get random health '''
    def get(self, request):
        random_health = Health.objects.order_by('?').first()
        serializer_data = HealthSerializer(random_health).data

        return Response(serializer_data)


class HobbyRandomAPIView(APIView):
    ''' Get random hobby '''
    def get(self, request):
        random_hobby = Hobby.objects.order_by('?').first()
        serializer_data = HobbySerializer(random_hobby).data

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
        random_trait = Trait.objects.order_by('?').first()
        serializer_data = TraitSerializer(random_trait).data

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
        random_baggage = Baggage.objects.order_by('?').first()
        serializer_data = BaggageSerializer(random_baggage).data

        return Response(serializer_data)


class AdditionalInfoRandomAPIView(APIView):
    ''' Get random additional information '''
    def get(self, request):
        random_info = AdditionalInfo.objects.order_by('?').first()
        serializer_data = AdditionalInfoSerializer(random_info).data

        return Response(serializer_data)