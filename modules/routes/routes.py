import os
from PIL import Image

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_modules = os.path.dirname(ruta_actual)
ruta_padre = os.path.dirname(ruta_modules)

ruta_carpeta_assets = os.path.join(ruta_padre, 'assets')

ruta_imagenPresentacion = os.path.join(ruta_carpeta_assets, 'presentacion.png')

ruta_logoServiExpress = os.path.join(ruta_carpeta_assets, 'logo.png')

ruta_iconUsuario = os.path.join(ruta_carpeta_assets, 'user.png')

ruta_iconPassword = os.path.join(ruta_carpeta_assets, 'pass.png')

imagenes = {
    'imagenPresentacion': Image.open(ruta_imagenPresentacion),
    'logoServiExpress': Image.open(ruta_logoServiExpress),
    'iconUsuario': Image.open(ruta_iconUsuario),
    'iconPassword': Image.open(ruta_iconPassword),
}