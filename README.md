# Certamen N°2: Fundación Patrimonio Vivo

Aplicación web desarrollada con Python y Django Framework para centralizar, gestionar y difundir el catálogo digital de lugares patrimoniales de la Fundación Patrimonio Vivo. Proyecto correspondiente al Certamen N°2 de la asignatura Taller Lenguaje de Programación (Ingeniería en Informática, USM).

## Descripción del Proyecto

El sistema permite que visitantes y usuarios autenticados consulten lugares patrimoniales registrados, revisen sus características detalladas y exploren el catálogo clasificado por categorías. Incluye un módulo de administración y áreas de gestión restringidas para usuarios con permisos específicos.

## Requisitos del Proyecto Implementados

- **RF01:** Página principal con presentación de la fundación y acceso directo al catálogo.
- **RF02:** Catálogo patrimonial dinámico basado en registros de la base de datos.
- **RF03:** Vista de detalle individual con información completa del lugar.
- **RF04 y RF05:** Clasificación de lugares por tipo de patrimonio y filtrado por categoría.
- **RF06:** Administración y gestión completa de categorías y lugares desde el panel de Django Admin.
- **RF07:** Interfaz estructurada mediante templates reutilizables y recursos estáticos locales (CSS/JS).
- **RF08 y RF09:** Autenticación de usuarios (inicio y cierre de sesión).
- **RF10, RF11 y RF12:** Acceso restringido a secciones de gestión y control estricto de autorización para agregar o modificar registros patrimoniales.

## Requisitos Previos

- Python 3.10 o superior instalado.
- Git instalado en el equipo.

## Instrucciones de Instalación y Ejecución

Sigue los siguientes pasos en tu terminal para clonar y ejecutar el proyecto localmente:

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/CER2-APELLIDONOMBRE.git
cd CER2-APELLIDONOMBRE
```

### 2. Crear y activar el entorno virtual

**En Windows (CMD o PowerShell):**

```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

Instala los paquetes necesarios utilizando el archivo de requerimientos:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos (Migraciones)

Ejecuta las migraciones de Django para preparar la base de datos SQLite y las tablas de los modelos (`Categoria` y `LugarPatrimonial`):

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un superusuario

Para acceder al panel de administración y gestionar los registros de la fundación:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para ingresar usuario, correo electrónico y contraseña.

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Acceder a la aplicación

Abre tu navegador web e ingresa a la siguiente dirección:

```text
http://127.0.0.1:8000/
```

## Tecnologías Utilizadas

- **Python / Django Framework:** Patrón MVT, ORM, autenticación y sistema de autorización.
- **Bootstrap 5:** Diseño responsivo de componentes.
- **HTML5 / CSS3:** Estructura y estilos estáticos personalizados.
- **SQLite:** Base de datos relacional.