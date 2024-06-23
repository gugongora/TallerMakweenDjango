from django.shortcuts import render

from .models import Cliente,Genero,Usuario

# Create your views here.

def index(request):
    clientes= Cliente.objects.all()
    context={"clientes":clientes}
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
    clientes = Cliente.objects.all()
    context={"clientes": clientes}
    return render(request, 'taller/clientes_list.html', context)

def clientesAdd(request):
    if request.method != "POST":
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'taller/clientes_add.html', context)
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
        obj=Cliente.objects.create( rut=rut,
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
        return render(request, 'taller/clientes_add.html', context)
    
def clientes_del(request,pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje="Bien, datos eliminados ..."
        clientes=Cliente.objects.all()
        context = {'alumnos': clientes, 'mensaje': mensaje}
        return render(request, 'taller/clientes_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'taller/clientes_list.html', context)
    

def clientes_findEdit(request,pk):

    if pk != "":
        cliente=Cliente.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(cliente.id_genero.genero))

        context={'cliente':cliente, 'generos':generos}
        if cliente:
            return render(request, 'taller/clientes_list.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'taller/clientes_list.html', context)
        
def clientesUpdate(request):

    #Es un POST, por lo tanto se recuperan los datos del formulario
    #y se graban en la tabla.
    if request.method == "POST":

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

        cliente = Cliente()
        cliente.rut=rut
        cliente.nombre=nombre
        cliente.apellido_paterno=aPaterno
        cliente.apellido_materno=aMaterno
        cliente.fecha_nacimiento=fechaNac
        cliente.id_genero=objGenero
        cliente.telefono=telefono
        cliente.email=email
        cliente.direccion=direccion
        cliente.activo=1
        cliente.save()

        generos=Genero.objects.all()
        context={'mensaje': "Ok, datos actualizdos...", 'generos':generos, 'cliente':cliente}
        return render(request, 'taller/clientes_edit.html', context)
    else:
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        clientes = Cliente.objects.all()
        context={'clientes':clientes}
        return render(request, 'taller/clientes_list.html', context)

