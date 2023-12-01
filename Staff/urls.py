from django.urls import path
from Staff.views import manage_admin, manage_doctor, manage_slots, vitals, manage_consultation
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', manage_doctor.homepage, name='homepage'),
    path('user/admin/dashboard', manage_admin.admin_dashboard, name='admin_dashboard'),
    path('Doctor/', manage_doctor.doctor_dashboard, name='Doctor'),
    path('Slot/', manage_slots.manage_slot, name='Slot'),
    path('FrontDesk/', manage_doctor.med_prof_onboarding, name='FrontDesk'),
    path('Doctor/speech-to-text/', manage_doctor.speech_to_text, name='speech-to-text'),
    # path('transcribe_audio', manage_doctor.transcribe_audio, name='transcribe_audio'),
    path('Medical-Professional-Onboarding/', manage_doctor.med_prof_onboarding, name='Medical-Professional-Onboarding'),

    path('Doctor/consultation/', manage_consultation.doctor_cons_list, name='doctor-consultation-list'),
    path('Doctor/consultation/<int:appointment_id>/', manage_consultation.doctor_consultation, name='doctor-consultation'),
    # path('Doctor/consultation/<int:nxt>/', manage_doctor.doctor_consultation, name='doctor-consultation1'),
    path('Doctor/vitals/', vitals.vitals_modal_insert, name='vitals_insert'),
    path('Doctor/symptoms/', vitals.symptoms_modal_insert, name='symptoms_insert'),
    path('Doctor/pre-existings/', vitals.preexisting_modal_insert, name='preexisting_modal_insert'),
    path('Doctor/upload_documents/', vitals.upload_documents, name='upload_documents'),
    path('Doctor/diagnosis/', vitals.diagnosis_modal_insert, name='diagnosis_modal_insert'),
    path('Doctor/prescription/', vitals.save_prescription, name='save_prescription'),
    path('Doctor/speech-to-text/', manage_doctor.speech_to_text, name='speech-to-text'),
    path('get_data/Vitals/', vitals.get_vitals, name='get_vitals'),
]
