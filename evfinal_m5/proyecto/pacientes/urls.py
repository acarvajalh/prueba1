from django.urls import path
from . import views

urlpatterns = [    
    path('inicio/', views.inicio, name="inicio"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('contacto/', views.contacto, name="contacto"),
    path('paciente_examen/', views.paciente_examen, name="paciente_examen"),
    path('paciente_hora/', views.paciente_hora, name="paciente_hora"),
    path('paciente_tratamiento/', views.paciente_tratamiento, name="paciente_tratamiento"),
    path('formulario/', views.ingresar_paciente, name ='ingresar_paciente'),
]
