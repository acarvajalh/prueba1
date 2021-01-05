from django.shortcuts import render,redirect
#from django.http import HttpResponseRedirect
from .forms import Form_Usuario
from .forms import Form_Tratamiento
from .forms import Form_Login
from .forms import Form_Examen
from django.conf import settings
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

def ingresar_paciente(request):
    form = Form_Usuario(request.POST or None)
    context = {'formulario': form}
    if form.is_valid():
        form_data = form.cleaned_data
        form_data['fecha_nacimiento']=form_data['fecha_nacimiento'].strftime("%Y-%m-%d")
        filename= "/pacientes/static/pacientes/data/formulario.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            pacientes=json.load(file)
        form_data['id'] = pacientes['ultimo_id_generado'] + 1
        pacientes['ultimo_id_generado'] = form_data['id']
        pacientes['pacientes'].append(form_data)   
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(pacientes, file)
        return redirect('pacientes:crear_exitoso')
    return render(request, 'pacientes/formularios.html', context)
    
def crear_exitoso(request):
    filename= "/pacientes/static/pacientes/data/formulario.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        pacientes=json.load(file)
    return render(request, 'pacientes/crear_exitoso.html', context=pacientes)

def eliminar_paciente(request, id):
    if request.method == "POST":
        filename= "/pacientes/static/pacientes/data/formulario.json"
        with open(str(settings.BASE_DIR)+filename, "r") as file:
            pacientes=json.load(file)

        for paciente in pacientes['pacientes']:
            print(int(paciente['id']), int(id))
            if int(paciente['id']) == int(id):
                pacientes['pacientes'].remove(paciente)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(pacientes, file)
        return redirect('pacientes:crear_exitoso')
    context = {'id': id} 
    return render(request, "pacientes/eliminar_paciente.html", context)

def paciente_tratamiento(request):
    filename= "/pacientes/static/pacientes/data/tratamientos.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        tratamientos=json.load(file)
    return render(request, 'pacientes/paciente_tratamiento.html', context=tratamientos)

def ingresar_tratamiento(request):
    form = Form_Tratamiento(request.POST or None)
    context = {'tratamientos': form}
    if form.is_valid():
        form_data = form.cleaned_data
        form_data['fecha']=form_data['fecha'].strftime("%Y-%m-%d")
        form_data['control']=form_data['control'].strftime("%Y-%m-%d")
        filename= "/pacientes/static/pacientes/data/tratamientos.json"

        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            tratamientos=json.load(file)
        form_data['id'] = tratamientos['ultimo_id_generado'] + 1
        tratamientos['ultimo_id_generado'] = form_data['id']
        tratamientos['tratamientos'].append(form_data)   
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(tratamientos, file)
        return redirect('pacientes:paciente_tratamiento')
    return render(request, 'pacientes/ingresar_tratamiento.html', context)

def paciente_examen(request):
    lista = []
    filename= "/pacientes/static/pacientes/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        examenes=json.load(file)
       # diccionario = examenes.get('examenes')
        #for elemento in diccionario:
           #resultado = elemento.get('id')
           #lista.append(resultado)
    #context = {'valor' : lista,'examenes':examenes, 'id': id}
    return render(request, 'pacientes/paciente_examen.html', context = examenes)

def iniciar_sesion(request):
    form = Form_Login(request.POST or None)
    context = {'usuarios': form}
    if form.is_valid():
        form_data = form.cleaned_data        
        filename= "/pacientes/static/pacientes/data/usuarios.json"    
        with open(str(settings.BASE_DIR)+filename, 'r') as file: 
            usuarios=json.load(file)               
        if usuarios['usuario'] == form_data['usuario'] and usuarios['contrasena'] == form_data['contrasena']:                
            return redirect('pacientes:pacientes')
    return render(request, 'pacientes/iniciar_sesion.html', context)


def ingresar_examen(request):
    form = Form_Examen(request.POST or None)
    context = {'examen': form}
    if form.is_valid():
        form_data = form.cleaned_data
        form_data['fecha']=form_data['fecha'].strftime("%Y-%m-%d")
        
        filename= "/pacientes/static/pacientes/data/examen.json"

        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            examenes=json.load(file)
        form_data['id'] = examenes['ultimo_id_generado'] + 1
        examenes['ultimo_id_generado'] = form_data['id']
        examenes['examenes'].append(form_data)   
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(examenes, file)
        return redirect('pacientes:paciente_examen')
    return render(request, 'pacientes/ingresar_examen.html', context) 


def grafico2(request):
    lista = []
    
    filename= "/pacientes/static/pacientes/data/examen.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        examenes=json.load(file)
        diccionario = examenes.get('examenes')
        for elemento in diccionario[-5:]:
            resultado = elemento.get('resultado')
            
            lista.append(resultado)
            

    context = {'valor' : lista}
    
    return render(request, "pacientes/grafico2.html", context)
