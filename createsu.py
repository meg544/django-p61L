import os
import django

# Configurar entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "meg_544@yahoo.com.mx"
password = "rabanito"
print("✅ si ejecuto Procfile.")
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("✅ Superusuario creado con éxito.")
else:
    print("⚠️ El superusuario ya existe.")
