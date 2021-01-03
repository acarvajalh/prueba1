from django.urls import path
from . import views

app_name = "pacientes"

urlpatterns = [    
    path('inicio/', views.inicio, name="inicio"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('contacto/', views.contacto, name="contacto"),
    path('paciente_examen/', views.paciente_examen, name="paciente_examen"),
    path('paciente_hora/', views.paciente_hora, name="paciente_hora"),
    path('paciente_tratamiento/', views.paciente_tratamiento, name="paciente_tratamiento"),
    path('formulario/', views.ingresar_paciente, name ="formulario"),
    path('ingresar_tratamiento/', views.ingresar_tratamiento, name ="ingresar_tratamiento"),
    path('crear_exitoso/', views.crear_exitoso, name="crear_exitoso"),
    path('<id>/borrar', views.eliminar_paciente, name="eliminar_paciente"),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
    path('ingreso_examen/', views.ingresar_examen, name="ingreso_examen"),
]
