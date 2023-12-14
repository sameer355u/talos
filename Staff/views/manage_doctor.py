from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from CustomAuth.models import ProfessionalType, User
from allauth.socialaccount.models import SocialApp

from Staff.create_initial_recors import create_admin, insert_mst_records, insert_menu_items
from Staff.models.professional_Onboarding import MstFlag
from CustomAuth.utility import get_user_menu


def homepage(request):
    # create_admin()
    # insert_mst_records(request)
    # insert_menu_items()

    menu_items = None
    if request.user.is_authenticated:
        menu_items = get_user_menu(request)
    return render(request, 'homepage.html', {'menu_items': menu_items})


@login_required(login_url="/accounts/login/")
# @allowed_role_users(allowed_roles='1001')
@permission_required('Doctor_dashboard')
def doctor_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')


@login_required(login_url="/accounts/login/")
def med_prof_onboarding(request):
    data = get_user_menu(request)
    return render(request, 'Medical-Professional-Onboarding.html',  {'data': data})


def speech_to_text(request):
    return render(request, 'speech-to-text.html')
