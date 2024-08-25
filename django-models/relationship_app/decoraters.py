from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

def custom_user_passes_test(test_func, redirect_url=None, error_message=None):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            if error_message:
                messages.error(request, error_message)
            return redirect(redirect_url or reverse('login'))
        return _wrapped_view
    return decorator