from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware que obliga a que el usuario esté autenticado para acceder a cualquier página,
    excepto aquellas especificadas en `LOGIN_EXEMPT_URLS`.
    """

    def process_request(self, request):
        # Lista de URLs exentas de autenticación
        exempt_urls = getattr(settings, 'LOGIN_EXEMPT_URLS', [])

        # Si el usuario ya está autenticado o la URL está en las exentas, permitimos el acceso
        if request.user.is_authenticated or self.is_url_exempt(request.path, exempt_urls):
            return None

        # Redirigir al inicio de sesión si el usuario no está autenticado
        return redirect(settings.LOGIN_URL)

    def is_url_exempt(self, path, exempt_urls):
        """
        Comprueba si la URL actual está exenta de autenticación.
        """
        from django.urls import reverse
        from urllib.parse import urlparse

        # Normalizamos las rutas de URLs exentas
        path = path.lstrip('/')
        for url in exempt_urls:
            if path == url.lstrip('/'):
                return True

        # También comprobamos si la URL actual coincide con alguna vista nombrada
        for url in exempt_urls:
            try:
                if path == reverse(url).lstrip('/'):
                    return True
            except:
                pass
        return False
