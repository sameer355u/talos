from CustomAuth.models import User
from django.db import models
from Staff.models.clinic import Clinic
from Staff.models.professional_Onboarding import HealthProfessionalPersonalDetails, MstHealthProfessional


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
    DoctorIdFK = models.ForeignKey(MstHealthProfessional, on_delete=models.RESTRICT)
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
