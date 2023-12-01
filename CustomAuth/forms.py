from CustomAuth.models import ProfessionalType, User
from allauth.account.forms import SignupForm
from django import forms


def check_phone(phone_number):
    if User.isExistsPhone(phone_number):
        raise forms.ValidationError('This phone number is already in use.')
    return phone_number


class ProfessionalsSignupForm(SignupForm):
    phone = forms.CharField(max_length=10, min_length=10, required=True, label='Phone number',
                            widget=forms.TextInput(attrs={'placeholder': '10 Digit Phone number'}))
    professional_type = forms.ModelChoiceField(queryset=ProfessionalType.get_professions(),
                                               label="Professional Type",
                                               widget=forms.Select(
                                                   attrs={'class': '', 'placeholder': 'Professional Type',}))

    class Meta:
        field_order = ['professional_type', 'email', 'phone', "password1", "password2"]

    @property
    def username_field(self):
        return "email"


class PatientSignupForm(SignupForm):
    phone = forms.CharField(max_length=10, min_length=10, required=True, label='Phone number',
                            widget=forms.TextInput(attrs={'placeholder': '10 Digit Phone number'}))

    def clean_phone_number(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError('This phone number is already in use.')
        return phone

    @property
    def username_field(self):
        return "email"
