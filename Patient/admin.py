from django.contrib import admin
from Patient.models.appointment import Appointment
from Patient.models.patient import MstPatient, MstPatientContact, MstPatientMedicalHistory, MstPatientPaymentDetails

admin.site.register(MstPatient)
admin.site.register(MstPatientContact)
admin.site.register(MstPatientMedicalHistory)
admin.site.register(MstPatientPaymentDetails)
admin.site.register(Appointment)
