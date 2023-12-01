from allauth.account.adapter import DefaultAccountAdapter
from CustomAuth.models import ProfessionalType


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        if request.method == 'POST' and 'Patient' in request.POST:
            user.profession = ProfessionalType.get_patient_profession_obj()  # id=2 for Patient only.
        elif request.method == 'POST' and 'Others' in request.POST:
            user.profession = form.cleaned_data.get("professional_type")
        user.phone = form.cleaned_data.get("phone")
        super().save_user(request, user, form, commit=commit)
