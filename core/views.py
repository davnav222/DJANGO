from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Cliente, Venta, Seccion
from .models import Configuracion

# --- INICIO ---
def inicio(request):
    return render(request, 'inicio.html')

# --- SECCIONES ---
def lista_secciones(request):
    return render(request, 'secciones_lista.html', {'secciones': Seccion.objects.all()})

def alta_seccion(request):
    if request.method == "POST":
        Seccion.objects.create(nombre=request.POST.get('nombre'))
        return redirect('lista_secciones')
    return render(request, 'secciones_alta.html')

def borrar_seccion(request, id):
    get_object_or_404(Seccion, id=id).delete()
    return redirect('lista_secciones')


# --- CLIENTES ---
def lista_clientes(request):
    return render(request, 'clientes_lista.html', {'clientes': Cliente.objects.all()})

def alta_cliente(request):
    if request.method == "POST":
        Cliente.objects.create(nombre=request.POST.get('nombre'))
        return redirect('lista_clientes')
    return render(request, 'clientes_alta.html')

def borrar_cliente(request, id):
    get_object_or_404(Cliente, id=id).delete()
    return redirect('lista_clientes')


# --- PRODUCTOS ---
def lista_productos(request):
    return render(request, 'productos_lista.html', {'productos': Producto.objects.all()})

def alta_producto(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST.get('nombre'),
            precio=request.POST.get('precio'),
            seccion_id=request.POST.get('seccion'),
            stock=request.POST.get('stock') # Guarda el stock inicial
        )
        return redirect('lista_productos')
    contexto = {'secciones': Seccion.objects.all()}
    return render(request, 'productos_alta.html', contexto)

def borrar_producto(request, id):
    get_object_or_404(Producto, id=id).delete()
    return redirect('lista_productos')


# --- VENTAS ---
def lista_ventas(request):
    fecha_busqueda = request.GET.get('fecha') # Capturamos la fecha del buscador
    
    if fecha_busqueda:
        # Filtramos las ventas que coincidan con esa fecha exacta
        ventas = Venta.objects.filter(fecha__date=fecha_busqueda)
    else:
        # Si no hay búsqueda, mostramos todas
        ventas = Venta.objects.all()
    
    return render(request, 'ventas_lista.html', {
        'ventas': ventas, 
        'fecha_busqueda': fecha_busqueda
    })
    
def alta_venta(request):
    if request.method == "POST":
        p_id = request.POST.get('producto')
        cant = int(request.POST.get('cantidad'))
        
        # 1. Creamos la venta
        Venta.objects.create(
            codigo=request.POST.get('codigo'),
            cliente_id=request.POST.get('cliente'),
            producto_id=p_id,
            cantidad=cant
        )
        
        # 2. RESTAMOS EL STOCK
        producto = Producto.objects.get(id=p_id)
        producto.stock -= cant # Resta la cantidad vendida
        producto.save()
        
        return redirect('lista_ventas')
    
    contexto = {
        'clientes': Cliente.objects.all(),
        'productos': Producto.objects.all(),
    }
    return render(request, 'ventas_alta.html', contexto)
    contexto = {
        'clientes': Cliente.objects.all(),
        'productos': Producto.objects.all(),
    }
    return render(request, 'ventas_alta.html', contexto)

def borrar_venta(request, id):
    get_object_or_404(Venta, id=id).delete()
    return redirect('lista_ventas')
    
def configuracion(request):
    config, created = Configuracion.objects.get_or_create(id=1)
    
    if request.method == "POST":
        config.nombre_empresa = request.POST.get('nombre')
        config.cif = request.POST.get('cif')
        config.direccion = request.POST.get('direccion')
        config.iva_general = request.POST.get('iva')
        config.save()
        return redirect('inicio')
        
    return render(request, 'configuracion.html', {'config': config})
