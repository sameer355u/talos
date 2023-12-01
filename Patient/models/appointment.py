from Patient.models.patient import MstPatient
from CustomAuth.models import User, ProfessionalType
from django.db import models
from Staff.models.doctor import TblDoctorSchedule, TblDoctorSlot
from django.contrib.auth.models import Group
from Staff.models.professional_Onboarding import HealthProfessionalPersonalDetails


class Appointment(models.Model):
    AppointmentIDPK = models.AutoField(primary_key=True)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    PatientIDFK = models.ForeignKey(MstPatient, on_delete=models.RESTRICT)
    Date = models.DateField()
    Time = models.TimeField()
    # ProfessionalTypeIDFK = models.ForeignKey(ProfessionalType, on_delete=models.RESTRICT)
    DoctorIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    SlotIDFK = models.ForeignKey(TblDoctorSlot, on_delete=models.RESTRICT)
    Active = models.CharField(default='A')
    BookingType = models.CharField(max_length=50)
    AppointmentType = models.CharField(max_length=50)
    AppointmentBy = models.CharField(max_length=50)
    CenterType = models.CharField(max_length=50)
    CreatedBy = models.CharField(max_length=8)
    UpdatedBy = models.CharField(max_length=8)
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
