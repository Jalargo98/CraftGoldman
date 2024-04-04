from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def only_admin_access(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Acceso no autorizado solo administradores.")
            return redirect('index')
    return _wrapped_view