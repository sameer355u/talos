import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_fun


def allowed_group_users(allowed_group=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_group:
                return view_fun(request, *args, **kwargs)
            else:
                return HttpResponse('You are not Authorized user')
        return wrapper_fun
    return decorator
#@allowed_group_users(allowed_group=['Staff-Group',''])


def allowed_role_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            print(datetime.datetime.now())
            user_roles = []
            for i in request.user.user_permissions.all():
                user_roles.append(i.id)
            print(user_roles)
            print(datetime.datetime.now())

            if allowed_roles in user_roles:
                print(datetime.datetime.now())
                return view_fun(request, *args, **kwargs)
            else:
                print(datetime.datetime.now())
                return HttpResponse('You are not Authorized user')
        return wrapper_fun
    return decorator
#@allowed_role_users(allowed_roles=64)


def admin_only(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all[0].name

        if group == 'admin':
            return view_fun(request, *args, **kwargs)
        elif group == 'Staff-Group':
            return redirect('Staff')
        elif group == 'Patient-Group':
            return redirect('Patient')
        elif group == 'Clinic-Group':
            return redirect('Clinic')
    return wrapper_fun
#@admin_only