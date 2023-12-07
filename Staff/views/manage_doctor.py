from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from CustomAuth.models import ProfessionalType, User
from allauth.socialaccount.models import SocialApp
from Staff.models.professional_Onboarding import MstFlag
from CustomAuth.utility import get_user_menu


def homepage(request):
    # try:
    #     professions = ['Admin', 'Patient', 'Doctor', 'Front-Desk']
    #     for i in professions:
    #         po = ProfessionalType(name=i)
    #         po.save()
    #     p = ProfessionalType.objects.get(name='Admin')
    
    #     phone = 8888888888
    #     pa = 'adminadmin'
    #     password = make_password(pa)
    #     email = 'admin@dnits.com'
    
    #     user = User(profession=p, phone=phone, password=password, email=email, is_superuser=True, is_staff=True)
    #     user.save()
    
    #     s = SocialApp(
    #         provider='google',
    #         name='Google SSO',
    #         client_id='341096323111-gls9q9l55dthp0bb1rne0kl3o3q4fah5.apps.googleusercontent.com',
    #         secret='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',
    #         settings='{}')
    #     s.save()
    # except:
    #     pass
    # ######## MST-Flag Entries: ------
    # mst_data = [[1,'SpecializationType',' Anaesthesia','Anaesthesia','A'],
    #             [2,'SpecializationType',' BAMS','BAMS','A'],
    #             [3,'SpecializationType','Cardiology','Cardiology','A'],
    #             [4,'SpecializationType','Dentist/BDS','Dentist/BDS','A'],
    #             [5,'SpecializationType','Diabetologist','Diabetologist','A'],
    #             [6,'SpecializationType','Dietician','Dietician','A'],
    #             [7,'SpecializationType','Endocrinology','Endocrinology','A'],
    #             [8,'SpecializationType','ENT','ENT','A'],
    #             [9,'SpecializationType','Gastroenterologist','Gastroenterologist','A'],
    #             [10,'EducationType','X','X','A'],
    #             [11,'Certifications','License','License','A'],
    #             [12,'HealthProfessionalDocumentType','State Medical Council Registration','Registration','A'],
    #             [13,'HealthProfessionalDocumentType','Healthcare Professional Registry','HPR','A'],
    #             [14,'HealthProfessionalDocumentType','No Objection Certificate','No Objection Certificate','A'],
    #             [15,'Certifications','Internship Completion Certificate','Internship Certificate','A'],
    #             [16,'HealthProfessionalDocumentType','Aadhar','Aadhar','A'],
    #             [17,'HealthProfessionalDocumentType','Marksheet','MBBS Degree','A'],
    #             [18,'HealthProfessionalDocumentType','Digital Signature','Digital Signature','A'],
    #             [19,'HealthProfessionalDocumentType','PAN Card','PAN Card','A'],
    #             [20,'HealthProfessionalDocumentType','Others','Others','A'],
    #             [21,'NurseType','Registered Auxilliary Nurse Midwife','Registered Auxilliary Nurse Midwife','A'],
    #             [22,'NurseType','Registered Nurse and Registered Midwife','Registered Nurse and Registered Midwife','A'],
    #             [23,'NurseType','Registered Nurse','Registered Nurse','A'],
    #             [24,'NurseType','Registered Lady Health Visitor','Registered Lady Health Visitor','A'],
    #             [25,'SpecializationType','General surgeon','General surgeon','A'],
    #             [26,'SpecializationType','MDS','MDS','A'],
    #             [27,'SpecializationType','Medicine','Medicine','A'],
    #             [28,'SpecializationType','Neurology','Neurology','A'],
    #             [29,'SpecializationType','Obstetrician/ Gynaecologist','Obstetrician/ Gynaecologist','A'],
    #             [30,'SpecializationType','Ophthalmology','Ophthalmology','A'],
    #             [31,'SpecializationType','Paediatrics','Paediatrics','A'],
    #             [32,'SpecializationType','Psychiatry','Psychiatry','A'],
    #             [33,'SpecializationType','Psychologist','Psychologist','A'],
    #             [34,'SpecializationType','Pulmonology','Pulmonology','A'],
    #             [35,'SpecializationType','Rheumatologist/Immunologist','Rheumatologist/Immunologist','A'],
    #             [36,'SpecializationType','Geriatric medicine','Geriatric medicine','A'],
    #             [37,'SpecializationType','Urologist','Urologist','A'],
    #             [38,'SpecializationType','Paediatric endocrinologist','Paediatric endocrinologist','A'],
    #             [39,'SpecializationType','Oncologist','Oncologist','A'],
    #             [40,'SpecializationType','Physiotherapist','Physiotherapist','A'],
    #             [41,'SpecializationType','MD ayurveda','MD ayurveda','A'],
    #             [42,'SpecializationType','IVF specialist','IVF specialist','A'],
    #             [43,'SpecializationType','Emergency medicine','Emergency medicine','A'],
    #             [44,'SpecializationType','Haematologist','Haematologist','A'],
    #             [45,'SpecializationType','Orthopaedician','Orthopaedician','A'],
    #             [46,'SpecializationType','General physician','General physician','A'],
    #             [47,'EducationType','XII','XII','A'],
    #             [48,'EducationType','UG','UG','A'],
    #             [49,'EducationType','PG','PG','A'],
    #             [50,'EducationType','Others','Others','A'],
    #             [51,'Certifications','Others','Others','A']]

    # for i in range(len(mst_data)):
    #     print(f'{i} : ', mst_data[i])
    #     mst_flag = MstFlag(FlagID=mst_data[i][0],
    #                        FlagName=mst_data[i][1],
    #                        FlagValue=mst_data[i][2],
    #                        FlagDesc=mst_data[i][3],
    #                        ActiveFlag='A',
    #                        CreatedBy=request.user.id,
    #                        UpdatedBy=request.user.id,)
    #     try:
    #         mst_flag.save()
    #     except:
    #         pass
    data = None
    if request.user.is_authenticated:
        data = get_user_menu(request)
    return render(request, 'homepage.html', {'data': data})


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
