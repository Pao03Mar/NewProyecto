from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.
# views la funcinalidad programar con python
def inicio(request):
    return render(request,'index.html')

def crear(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'crear.html', {
        'proveedores': proveedores 
    })

def añadir(request):
    formulario = ProveedorForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crear')
    return render(request, 'añadir.html', {'formulario': formulario})

def editar(request, id):
    proveedor = Proveedor.objects.get(id=id)
    formulario = ProveedorForm(request.POST or None, instance=proveedor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('crear')
    return render(request, 'editar.html', {'formulario': formulario})

def eliminar(request, id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('crear')  # redirecciona a la vista index