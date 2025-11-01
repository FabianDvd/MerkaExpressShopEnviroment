

from django.urls import path #Importarmos los modulos

from . import views #Importar las vistas 

#urlpatterns Aray que contiene las urls 

urlpatterns= [ 

    
    path("registro/", views.Registro_usuario, name="registro"), #cuando alguien entre a registro se ejecutara la funcion de registro
    path('', views.Registro_usuario),
]