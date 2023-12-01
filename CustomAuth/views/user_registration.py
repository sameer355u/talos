from allauth.account.utils import send_email_confirmation
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from CustomAuth.utility import custom_validator
from CustomAuth.models import User, ProfessionalType
from django.shortcuts import render, redirect
from Staff.decorators import unauthenticated_user


@unauthenticated_user
def multi_signup(request):
    professions = ProfessionalType.get_professions
    return render(request, 'account/signup.html', {'professions': professions})


def signup_patient(request):
    professions = ProfessionalType.get_professions()
    if request.method == 'POST' and 'Patient' in request.POST:
        email = request.POST.get('patient_email')
        phone = request.POST.get('patient_phone')
        password = request.POST.get('patient_password')
        password_2 = request.POST.get('patient_password_2')
        value = {
            'email': email,
            'phone': phone,
            'professions': professions,
        }
        if password != password_2:
            return render(request, 'account/signup.html', {'error': 'Password must be same', 'value': value})
        error_message = None
        patient_profession = ProfessionalType.get_patient_profession_obj()
        #print("patient_profession", patient_profession)
        user_patient = User(username=patient_profession.name[0] + str(User.objects.all().count() + 1).zfill(6),
                            email=email,
                            phone=phone,
                            password=password,
                            profession=patient_profession)
        error_message = custom_validator(user_patient)
        if not error_message:
            user_patient.password = make_password(user_patient.password)
            user_patient.save()
            messages.warning(request, 'You have register successfully!')
            send_email_confirmation(request, user_patient, signup=False, email=user_patient.email)
            return redirect('account_login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'account/signup.html', data)
    else:
        return render(request, 'account/signup.html', {'professions': professions})


def signup_staff(request):
    professions = ProfessionalType.get_professions()
    if request.method == 'POST' and 'Staff' in request.POST:
        email = request.POST.get('staff_email')
        phone = request.POST.get('staff_phone')
        profession_id = request.POST.get('profession')
        first_name = request.POST.get('staff_first_name')
        last_name = request.POST.get('staff_last_name')
        dob = request.POST.get('staff_dob')
        password = request.POST.get('staff_password')
        password_2 = request.POST.get('staff_password_2')
        value = {
            'email': email,
            'phone': phone,
            'professions': professions,
        }
        if password != password_2:
            return render(request, 'account/signup.html', {'error': 'Password must be same', 'value': value})
        user_profession = ProfessionalType.get_profession_by_id(profession_id)
        user_staff = User(username=user_profession.name[0] + str(User.objects.all().count() + 1).zfill(6),
                          first_name=first_name,
                          last_name=last_name,
                          dob=dob,
                          email=email,
                          phone=phone,
                          password=password,
                          profession=ProfessionalType.get_profession_by_id(profession_id))
        error_message = custom_validator(user_staff)
        if not error_message:
            user_staff.password = make_password(user_staff.password)
            user_staff.save()
            messages.warning(request, 'You have register successfully!')
            send_email_confirmation(request, user_staff, signup=False, email=user_staff.email)
            return redirect('account_login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'account/signup.html', data)
    else:
        return render(request, 'account/signup.html', {'professions': professions})
