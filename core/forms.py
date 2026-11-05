# 1. Importamos la herramienta de formularios de Django
from django import forms
# 2. Importamos el modelo que queremos mapear
from .models import LugarPatrimonial

# 3. Creación de nuestra clase de formulario heredando de forms.ModelForm
class LugarPatrimonialForm(forms.ModelForm):
    
    # 4. Configuración de metadatos
    class Meta:
        #formulario es para la tabla LugarPatrimonial"
        model = LugarPatrimonial
        
        # columnas del modelo queremos mostrar en la web
        fields = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'imagen', 'categoria']
        
        # textos para los labels
        labels = {
            'nombre': 'Nombre del Lugar Patrimonial',
            'descripcion': 'Descripción Detallada',
            'ubicacion': 'Ubicación / Ciudad',
            'anio_construccion': 'Año de Construcción',
            'imagen': 'URL de la Imagen',
            'categoria': 'Categoría Asignada',
        }