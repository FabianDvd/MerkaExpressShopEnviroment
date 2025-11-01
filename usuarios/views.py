
from django.shortcuts import render,redirect # importar los shorcuts 
from django.http import HttpResponse

from .forms import Register # importar la clase de registro 


#Definir una funcion de respuesta al acceder a la url

def Registro_usuario(request):

    if request.method =="POST":
        Register_Form = Register(request.POST) #Clase del modelo 
        if Register_Form.is_valid():

            usuario = Register_Form.save(False) # evitar que se guarde aun 
            usuario.id_rol_id = 1 # Asignar
            Register_Form.save() #Guardar los datos del formulario 
            return redirect("login") # el path debe ser el login
    else:
        Register_Form = Register()
    return render(request,"registro.html", {"form": Register_Form})

        
