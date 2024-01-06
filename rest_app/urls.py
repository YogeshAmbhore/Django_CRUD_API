from django.urls import path
from .views import *

urlpatterns = [
    path('', get_home, name='home'),
    path('details/<int:pk>/', get_details, name='details'),
]