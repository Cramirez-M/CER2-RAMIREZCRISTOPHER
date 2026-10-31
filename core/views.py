from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial, Categoria
# Create your views here.

# Esta es la función que creas
def catalogo(request, id_cat=None):
    
    # Siempre traemos las categorías para dibujar los botones
    categorias_bd = Categoria.objects.all()

    # Preguntamos: ¿El usuario hizo clic en una categoría y nos mandó un número?
    if id_cat:
        # Buscamos en la BD donde la columna categoria_id sea igual al id_cat que llegó
        lugares = LugarPatrimonial.objects.filter(categoria_id=id_cat)
    else:
        # Si no mandó número, traemos todos los lugares
        lugares = LugarPatrimonial.objects.all()

    print("---------------------------------")
    print("ID RECIBIDO EN LA URL:", id_cat)
    print("LUGARES ENCONTRADOS:", lugares)
    print("---------------------------------")

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
    
    # Renderizamos el HTML pasándole el diccionario
    return render(request, 'core/detalle_lugar.html', data)

def base(request):
    return render(request, 'core/base.html')

def home(request):
    return render (request, 'core/home.html')
    