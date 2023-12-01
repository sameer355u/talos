from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from CustomAuth.models import ProfessionalType, User


def homepage(request):
    try:
        professions = ['Admin', 'Patient', 'Doctor', 'Front-Desk']
        for i in professions:
            po = ProfessionalType(name=i)
            po.save()
        p = ProfessionalType.objects.get(name='Admin')

        phone = 8888888888
        pa = 'adminadmin'
        password = make_password(pa)
        email = 'admin@dnits.com'

        user = User(profession=p, phone=phone, password=password, email=email, is_superuser=True, is_staff=True)
        user.save()
    except:
        pass
    return render(request, 'homepage.html')


@login_required(login_url="/accounts/login/")
# @allowed_role_users(allowed_roles='1001')
@permission_required('Doctor_dashboard')
def doctor_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'dashboard.html')


@login_required(login_url="/accounts/login/")
def med_prof_onboarding(request):
    return render(request, 'Medical-Professional-Onboarding.html')


def speech_to_text(request):
    return render(request, 'speech-to-text.html')
