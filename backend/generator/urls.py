from django.urls import path

from .views import GenderRandomAPIView, ProfessionRandomAPIView, HealthRandomAPIView, HobbyRandomAPIView, PhobiaRandomAPIView, TraitRandomAPIView, PhysiqueRandomAPIView, BaggageRandomAPIView, AdditionalInfoRandomAPIView, CatastropheRandomAPIView, BunkerItemsRandomAPIView, BunkerRoomsRandomAPIView

urlpatterns = [
    path('gender/', GenderRandomAPIView.as_view(), name='gender'),
    path('profession/', ProfessionRandomAPIView.as_view(), name='profession'),
    path('health/', HealthRandomAPIView.as_view(), name='health'),
    path('hobby/', HobbyRandomAPIView.as_view(), name='hobby'),
    path('phobia/', PhobiaRandomAPIView.as_view(), name='phobia'),
    path('trait/', TraitRandomAPIView.as_view(), name='trait'),
    path('physique/', PhysiqueRandomAPIView.as_view(), name='physique'),
    path('baggage/', BaggageRandomAPIView.as_view(), name='baggage'),
    path('info/', AdditionalInfoRandomAPIView.as_view(), name='info'),

    path('catastrophe/', CatastropheRandomAPIView.as_view(), name='catastrophe'),

    path('items/', BunkerItemsRandomAPIView.as_view(), name='items'),
    path('rooms/', BunkerRoomsRandomAPIView.as_view(), name='rooms'),
]