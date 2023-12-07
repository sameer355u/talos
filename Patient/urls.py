from django.urls import path
from Patient.views import manage_patient, manage_appointments

urlpatterns = [
    path('', manage_patient.index, name='Patient'),
    path('patient-registration/', manage_patient.patient_registration, name='patient_registration'),
    path('edit_patient_details/', manage_patient.edit_patient_details, name='edit_patient_details'),
    path('book-appointment/', manage_appointments.book_appointment, name='book-appointment'),
    path('book_appointment_for/<int:record_id>/', manage_appointments.book_appointment_for, name='book_appointment_for'),
    path('book_appointment/<int:doc_id>/<str:slot_date>/', manage_appointments.book_appointment_date_slot,
         name='book_appointment_date_slot'),
]
