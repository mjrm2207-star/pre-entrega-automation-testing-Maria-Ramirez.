# pre-entrega-automation-testing-Maria-Ramirez.
# Preentrega de automatización de pruebas — María Ramirez

Proyecto del curso de automatización, desarrollado con Python, Selenium y pytest.

# Objetivo

Automatizar y validar el inicio de sesión exitoso en SauceDemo: https://www.saucedemo.com/

# Prueba implementada

Archivo: `tests/test_sauce_login.py`

La prueba realiza las siguientes acciones:

1. Abre Google Chrome.
2. Accede a SauceDemo.
3. Ingresa las credenciales de prueba proporcionadas por el sitio.
4. Presiona el botón de inicio de sesión.
5. Verifica que la URL contenga `/inventory.html`.
6. Cierra el navegador al finalizar.

# Herramientas y requisitos

- Python.
- Google Chrome.
- Selenium.
- pytest.
- Conexión a Internet.

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
python -m pip install selenium pytest
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

# Estado actual

Se implementó una prueba de inicio de sesión exitoso.

La generación de reportes HTML y capturas está pendiente de implementación. La carpeta `datos/` se incorporará si se utilizan datos externos en archivos CSV o JSON.

# Autora

María Jose Ramirez.