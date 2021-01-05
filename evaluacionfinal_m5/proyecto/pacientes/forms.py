from django import forms

class Form_Usuario(forms.Form):
    Nombre = forms.CharField()
    Apellido= forms.CharField()
    Edad= forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    

class Form_Tratamiento(forms.Form):
    fecha = forms.DateField()
    diagnostico = forms.CharField()
    tratamiento= forms.CharField()
    control = forms.DateField()
    comentarios= forms.CharField()

class Form_Examen(forms.Form):
    fecha = forms.DateField()
    tipo = forms.CharField()
    nombre= forms.CharField()
    resultado= forms.IntegerField()
    rango= forms.CharField()
    id_paciente = forms.CharField()

class Form_Login(forms.Form):   
    usuario = forms.CharField()
    contrasena= forms.CharField(widget=forms.PasswordInput)
   
    