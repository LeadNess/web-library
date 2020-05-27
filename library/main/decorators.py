# pylint: disable=import-error, no-else-return
"""
Decorators for differentiate user rights
"""
from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    """
    Checked if user is authorized
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrapper_func


def allowed_users(allowed_roles: list):
    """
    Checked if user belong to allowed group

    :param allowed_roles: 'student' or 'lecturer'
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            is_allowed = False
            for group in allowed_roles:
                if request.user.groups.filter(name=group):
                    is_allowed = True

            if is_allowed:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not permitted to see this page.')
        return wrapper_func
    return decorator
