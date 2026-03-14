from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views # Esto es para que funcione el login por Token

urlpatterns = [
    # 1. La ruta para entrar al panel de administración de Django
    path('admin/', admin.site.urls),

    # 2. Aquí conectamos las rutas de tu app 'temperatures' 
    # Todo lo que empiece con /api/ se irá a temperatures/urls.py
    path('api/', include('temperatures.urls')),

    # 3. Esta ruta es para que los usuarios manden su usuario/contraseña 
    # y la API les regrese su TOKEN de seguridad.
    path('api-token-auth/', views.obtain_auth_token),
]