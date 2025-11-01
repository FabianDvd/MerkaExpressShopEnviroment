from django import forms

from .models import Usuarios 


class Register(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput, label="Contraseña") #Tal cual como se llama en el campo del modelo osea las llaves 
    class Meta :
        model = Usuarios
        fields = ["nombre_completo","correo_electronico","numero_celular","foto_perfil"]