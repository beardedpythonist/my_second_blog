from django.urls import path
from .views import *

urlpatterns = [path('', index11, name='home'),
               path('about/', about, name='about')]
