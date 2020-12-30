from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import PrimerFormulario
import json

# Create your views here.

def inicio(request):
    return render(request,'pacientes/inicio.html', )

def pacientes(request):
    return render(request,'pacientes/pacientes.html', )

def contacto(request):
    return render(request,'pacientes/contacto.html', )

def paciente_examen(request):
    return render(request,'pacientes/paciente_examen.html', )

def paciente_hora(request):
    return render(request,'pacientes/paciente_hora.html', )

def paciente_tratamiento(request):
    return render(request,'pacientes/paciente_tratamiento.html', )
'''
def ingresar_paciente(request):
    form = PrimerFormulario()
    context = {'formulario': form}
    return render(request,
                   'pacientes/formularios.html',
                   context = context)


'''
#######Create your views here.
def ingresar_paciente(request):
    form = PrimerFormulario(request.POST or None)
    context = {'form': formulario}
    if form.is_valid():
        form_data = form.cleaned_data
        form_data['fecha_nacimiento']=form_data['fecha_nacimiento'].strftime("%Y-%m-%d")
    filename= "/formularios/static/formularios/data/guitarras.json"
with open(str(settings.BASE_DIR)+filename, 'r') as file:
guitarras=json.load(file)
guitarras['guitarras'].append(form_data)
with open(str(settings.BASE_DIR)+filename, 'w') as file:
json.dump(guitarras, file)
return redirect('formularios:crear_exitoso')
return render(request, 'formularios/crear_guitarra.html', context)
def crear_exitoso(request):
filename= "/formularios/static/formularios/data/guitarras.json"
with open(str(settings.BASE_DIR)+filename, "r") as file:
guitarras=json.load(file)
return render(request, 'formularios/crear_exitoso.html', context=guitarras)
