from django.urls import path

from .views import ProffesionRandomAPIView

urlpatterns = [
    path('profession/', ProffesionRandomAPIView.as_view(), name='profession'),
]