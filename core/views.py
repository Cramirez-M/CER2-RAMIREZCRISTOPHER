from django.shortcuts import render, get_object_or_404, redirect
from .models import LugarPatrimonial, Categoria
from django.contrib.admin.views.decorators import staff_member_required
from .forms import LugarPatrimonialForm
# Create your views here.

def catalogo(request, id_cat=None):
    
    #traemos las categorías para dibujar los botones
    categorias_bd = Categoria.objects.all()

    # si el usuario clickeo una categoria envia una id
    if id_cat:
        # Buscamos en la BD donde la columna categoria_id sea igual al id_cat que llegó
        lugares = LugarPatrimonial.objects.filter(categoria_id=id_cat)
    else:
        #si no, mostramos todos los lugares
        lugares = LugarPatrimonial.objects.all()


    # Metemos todo a la mochila
    data = {
        'lista_lugares': lugares,
        'lista_categorias': categorias_bd
    }
    # 'render' toma la petición, busca el HTML y lo envía al navegador
    return render(request, 'core/catalogo.html', data)
    

def detalle_lugar(request, id):
    # Buscamos el registro exacto usando el id de la URL
    lugar_encontrado = get_object_or_404(LugarPatrimonial, id=id)
    
    # Empaquetamos la variable en el diccionario 'data'
    data = {
        'lugar': lugar_encontrado
    }
    
    return render(request, 'core/detalle_lugar.html', data)

def base(request):
    return render(request, 'core/base.html')

def home(request):
    return render (request, 'core/home.html')

@staff_member_required
def agregar_lugar(request):
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('catalogo')

    else:
        form = LugarPatrimonialForm()
    return render(request, 'core/agregar_lugar.html', {'form' : form})

@staff_member_required
def editar_lugar(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)

    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = LugarPatrimonialForm(instance=lugar)
    return render(request, 'core/editar_lugar.html', {'form': form})


# solo el personal autorizado
@staff_member_required
def eliminar_lugar(request, id):
    
    lugar = get_object_or_404(LugarPatrimonial, id=id)
    
    # 2. Preguntamos si el usuario envio datos por el formulario
    if request.method == 'POST':
        lugar.delete()
        # 4. Una vez borrado, redirigimos 
        return redirect('catalogo')
    
    # 5. Si el método NO es POST (es decir, el usuario solo hizo clic en el enlace para entrar a la página), mostramos el formulario.
    
    return render(request, 'core/eliminar_lugar.html', {'lugar': lugar})
    