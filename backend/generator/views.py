from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Proffesion
from .serializers import ProffesionSerializer


class ProffesionRandomAPIView(APIView):
    ''' Get random profession '''
    def get(self, request):
        random_proffesion = Proffesion.objects.order_by('?').first()
        serializer_data = ProffesionSerializer(random_proffesion).data

        return Response(serializer_data)