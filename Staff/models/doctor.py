from CustomAuth.models import User
from django.db import models
from Staff.models.clinic import Clinic
from Staff.models.professional_Onboarding import HealthProfessionalPersonalDetails


# class ClinicProfessional(models.Model):
#     class Meta:
#         db_table = 'staff"."ClinicProfessional'
#     clinic_Professional_id = models.AutoField(primary_key=True)
#     professional_Name = models.CharField(max_length=50, unique=True)
#     professional_Type = models.ForeignKey(Group, on_delete=models.RESTRICT)
#
#
# class Doctor(models.Model):
#     gender = [
#         (1, 'Male'),
#         (2, 'Female'),
#         (3, 'Others'),
#     ]
#     blood_group = [
#         (1, 'A+'),
#         (2, 'B+'),
#         (3, 'AB+'),
#         (4, 'O+'),
#         (5, 'A-'),
#         (6, 'B-'),
#         (7, 'AB-'),
#         (8, 'O-'),
#     ]
#     doctor_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.RESTRICT)
#     clinic = models.ForeignKey(Clinic, on_delete=models.RESTRICT)
#     doctor_type = models.CharField(max_length=50)
#     qualification = models.CharField(max_length=50)
#     gender = models.IntegerField(choices=gender, default='1')
#     blood_group= models.IntegerField(choices=blood_group)
#     phone = models.IntegerField(unique=True)
#     mail = models.EmailField(unique=True)
#     active = models.BooleanField(default=True)
#     created_by = models.CharField(max_length=8)
#     updated_by = models.CharField(max_length=8)
#     create_date = models.DateField(auto_now_add=True)
#     update_date = models.DateField(auto_now=True)
#
#     @staticmethod
#     def get_doctor_id(user):
#         return Doctor.objects.get(user=user)


class TblDoctorSchedule(models.Model):
    DoctorScheduleIdPK = models.AutoField(primary_key=True)
    DoctorIdFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    UserIdFK = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    ClinicIdFK = models.ForeignKey(Clinic, on_delete=models.RESTRICT)
    StartDate = models.DateField()
    EndDate = models.DateField()
    SlotDuration = models.IntegerField()
    Day = models.CharField(max_length=10)
    StartTime = models.TimeField()
    NoofSlots = models.IntegerField()
    active = models.BooleanField(default=True)
    CreatedBy = models.CharField(max_length=8)
    UpdatedBy = models.CharField(max_length=8)
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_schedule_by_id(DoctorScheduleIdPK):
        return TblDoctorSchedule.objects.get(DoctorScheduleIdPK=DoctorScheduleIdPK)

    @staticmethod
    def get_schedule(StartDate, Day, DoctorIdFK):
        return TblDoctorSchedule.objects.get(StartDate=StartDate, Day=Day, DoctorIdFK=DoctorIdFK)

    def __str__(self):
        return self.Day


class TblDoctorSlot(models.Model):
    DoctorSlotIdPK = models.AutoField(primary_key=True)
    DoctorIdFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    UserIdFK = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    ClinicIdFK = models.ForeignKey(Clinic, on_delete=models.RESTRICT)
    DoctorScheduleIdFK = models.ForeignKey(TblDoctorSchedule, on_delete=models.RESTRICT)
    SlotDate = models.DateField()
    Day = models.CharField(max_length=10)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Status = models.CharField(max_length=10)
    AppointmentIdFK = models.IntegerField()
    CreatedBy = models.CharField(max_length=8)
    UpdatedBy = models.CharField(max_length=8)
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)

    @staticmethod
    def getSlot_by_id(slot_id):
        return TblDoctorSlot.objects.get(DoctorSlotIdPK=slot_id)

    @staticmethod
    def getSlot(DoctorIdFK, SlotDate):
        return TblDoctorSlot.objects.filter(DoctorIdFK=DoctorIdFK, SlotDate=SlotDate)

    def __str__(self):
        return str(self.SlotDate)
