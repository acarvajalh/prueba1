from django import forms




class PrimerFormulario(forms.Form):
    Nombre = forms.CharField()
    Apellido= forms.CharField()
    Edad= forms.IntegerField()
    fecha_nacimiento = forms.DateField()
                
