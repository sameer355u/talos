from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('account_login')