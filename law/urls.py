from django.urls import path
from . import views



urlpatterns = [
    path('' , views.index , name='index'),
    path('conslut/' , views.conslut , name='conslut'),
    path('servece/' , views.services , name='services'),
    path('contact/' , views.contact , name='contact'),
    path('lawyer_guide/' , views.lawyer_guide , name='lawyer_guide'),
    path('library_law/' , views.library_law , name='library_law'),
]