from django.shortcuts import render

from .models import Alumno,Genero

# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'taller/index.html', context)

def footer(request):
    context={}
    return render(request, 'taller/footer.html', context)

def navbar(request):
    context={}
    return render(request, 'taller/navbar.html', context)

def mantencion(request):
    context={}
    return render(request, 'taller/mantencion.html', context)

def reparacion(request):
    context={}
    return render(request, 'taller/reparacion.html', context)

def refacciones(request):
    context={}
    return render(request, 'taller/refacciones.html', context)

def trabajos(request):
    context={}
    return render(request, 'taller/trabajos.html', context)

def equipo(request):
    context={}
    return render(request, 'taller/equipo.html', context)

def contacto(request):
    context={}
    return render(request, 'taller/contacto.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos':alumnos}
    return render(request, 'taller/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'taller/alumnos_add.html', context)
    else:
        
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"
        
        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create( rut=rut,
                                   nombre=nombre,
                                   apellido_paterno=aPaterno,
                                   apellido_materno=aMaterno,
                                   fecha_nacimiento=fechaNac,
                                   id_genero=objGenero,
                                   telefono=telefono,
                                   email=email,
                                   direccion=direccion,
                                   activo=1)
        obj.save()
        context={'mensaje': "Ok, datos grabados ..."}
        return render(request, 'taller/alumnos_add.html', context)
    
