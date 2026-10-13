# pre-entrega-automation-testing-Maria-Ramirez.

Proyecto del curso de automatización, desarrollado con Python, Selenium y pytest. 

# Objetivo

Automatizar y validar el inicio de sesión exitoso en SauceDemo: https://www.saucedemo.com/, verificar productos, agregar uno al carrito y hacer validaciones.

# Pruebas incluidas

El archivo: `tests/test_sauce_login.py` contiene ocho pruebas

1. Iniciar sesión con el usuario de prueba standard_user y verificar la redirección al inventario.
2. Validar el título de la página y el título de la sección de productos.
3. Comprobar que haya productos, que el primero esté visible y que muestre nombre y precio.
4. Verificar que el botón del menú y el filtro estén visibles.
5. Agregar el primer producto al carrito y comprobar que el botón cambie a Remove.
6. Validar que el contador del carrito muestre 1.
7. Abrir el carrito y verificar la URL.
8. Comprobar que el carrito contenga un producto con nombre y precio, e imprimir esos datos.

Las pruebas comparten una sesión de Chrome y continúan el mismo recorrido.

# Herramientas y requisitos

- Python.
- Google Chrome.
- Selenium.
- pytest.
- pytest-html

# Preparación del entorno

Desde la terminal de PowerShell, ubicada en la carpeta del proyecto:

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install selenium pytest pytest-html
```

Si el entorno virtual ya existe, solo es necesario activarlo e instalar las dependencias que falten.

# Ejecución de las pruebas

Desde la raíz del proyecto, con el entorno virtual activo:

```powershell
python -m pytest tests/test_sauce_login.py -v
```

Para ejecutar todas las pruebas de la carpeta `tests/`:

```powershell
python -m pytest tests/ -v
```

# Estructura del proyecto

- `tests/`: pruebas automatizadas.
- `utils/`: carpeta destinada a funciones auxiliares.
- `.gitignore`: exclusión del entorno virtual y archivos temporales.
- `README.md`: descripción e instrucciones del proyecto.

# Reporte HTML
Ejecutar las pruebas y generar el reporte: 
python -m pytest tests/test_sauce_login.py -v --html=reports/reporte.html --self-contained-html

El archivo reports/reporte.html contiene los resultados de esa ejecución. Para abrirlo en el navegador desde PowerShell:
Start-Process .\reports\reporte.html
Cada ejecución con este comando reemplaza el reporte anterior.

# Autora

María Jose Ramirez.