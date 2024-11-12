from django.urls import path

from .views import GenderRandomAPIView, ProffesionRandomAPIView, HealthRandomAPIView, HobbyRandomAPIView, PhobiaRandomAPIView, TraitRandomAPIView, PhysiqueRandomAPIView, BaggageRandomAPIView, InfoRandomAPIView

urlpatterns = [
    path('gender/', GenderRandomAPIView.as_view(), name='gender'),
    path('profession/', ProffesionRandomAPIView.as_view(), name='profession'),
    path('health/', HealthRandomAPIView.as_view(), name='health'),
    path('hobby/', HobbyRandomAPIView.as_view(), name='hobby'),
    path('phobia/', PhobiaRandomAPIView.as_view(), name='phobia'),
    path('trait/', TraitRandomAPIView.as_view(), name='trait'),
    path('physique/', PhysiqueRandomAPIView.as_view(), name='physique'),
    path('baggage/', BaggageRandomAPIView.as_view(), name='baggage'),
    path('info/', InfoRandomAPIView.as_view(), name='info'),
]