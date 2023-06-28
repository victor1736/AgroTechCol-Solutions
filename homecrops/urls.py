from homecrops.views import index, nosotros, portafolio, contacto, ceo
from django.urls import path
from django.urls import include


urlpatterns = [
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('portafolio/', portafolio, name='portafolio'),
    path('contacto/', contacto, name='contacto'),
    path('ceo/', ceo, name='ceo'),
]
