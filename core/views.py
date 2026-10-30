from django.shortcuts import render, get_object_or_404
from .models import LugarPatrimonial
# Create your views here.

# Esta es la función que creas
def catalogo(request):
    #con objects.all, recolectamos todos los datos de la BD (modelos)
    lugares = LugarPatrimonial.objects.all()

    #alamcenamos los datos en forma de diccionario
    data = {
        'lista_lugares' : lugares
    }
    print(data)
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
    