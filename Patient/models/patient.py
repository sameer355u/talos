from CustomAuth.models import User
from django.db import models
from datetime import date
from django.core.files.storage import FileSystemStorage
# from Staff.models.clinic import Clinic


class MstPatient(models.Model):
    RecordIDPK = models.AutoField(primary_key=True)
    PatientID = models.CharField(max_length=11)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    PatientProfileImage = models.ImageField(max_length=400)
    FirstName = models.CharField(max_length=30, default=None)
    MiddleName = models.CharField(max_length=30, default=None)
    LastName = models.CharField(max_length=30, default=None)
    GenderType = [('M', 'Male'), ('F', 'female'), ('O', 'Others')]
    Gender = models.CharField(max_length=9, choices=GenderType)
    BloodGroup = models.CharField(max_length=4, default=None)
    Nationality = models.CharField(max_length=15, default=None)
    AadharNo = models.BigIntegerField(default=78)
    MaritalStatustype = [('U', 'Unmarried'), ('Mrd', 'Married'), ('D', 'Divorcee'), ('W', 'Widow')]
    MaritalStatus = models.CharField(max_length=15, choices=MaritalStatustype)
    Address = models.CharField(max_length=75, default=None)
    City = models.CharField(max_length=25, default=None)
    State = models.CharField(max_length=30, default=None)
    Country = models.CharField(max_length=30, default=None)
    Pin = models.IntegerField()
    SpouseName = models.CharField(max_length=20, default=None)
    DOB = models.DateField()
    Age = models.IntegerField()
    ActiveFlag = models.CharField(max_length=3, default=None)
    CreatedBy = models.CharField(max_length=15, default='A')
    UpdatedBy = models.CharField(max_length=15, default='A')
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_patients():
            return MstPatient.objects.filter(ActiveFlag='A')

    @staticmethod
    def get_patient_by_id(record_id):
        return MstPatient.objects.get(RecordIDPK=record_id)

    @staticmethod
    def get_patient_by_patientId(PatientID):
        return MstPatient.objects.get(PatientID=PatientID, ActiveFlag='A')


class MstPatientContact(models.Model):
    id = models.AutoField(primary_key=True)
    RecordIDFK = models.ForeignKey(MstPatient, on_delete=models.RESTRICT)
    PatientID = models.CharField(max_length=11)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    PatientContactNumber = models.BigIntegerField(default=None)
    AlternatNumber = models.BigIntegerField(default=91)
    PatientEmailId = models.EmailField(max_length=50, default=None)
    EmergencyContactNumber = models.BigIntegerField()
    EmergencyContactName = models.CharField(max_length=21, default=None)
    EmergencyContactRelation = models.CharField(max_length=21, default=None)
    ActiveFlag = models.CharField(max_length=3, default=None)
    CreatedBy = models.CharField(max_length=15, default='A')
    UpdatedBy = models.CharField(max_length=15, default='A')
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_Patient_contact_by_record_id(record_id):
        return MstPatientContact.objects.get(RecordIDFK=record_id)


class MstPatientMedicalHistory(models.Model):
    id = models.AutoField(primary_key=True)
    RecordIDFK = models.ForeignKey(MstPatient, on_delete=models.RESTRICT)
    PatientID = models.CharField(max_length=11)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    PreExistingCondition = models.CharField(max_length=50, default=None)
    Description = models.TextField()
    MedicalRecordFile = models.URLField(max_length=400)
    Remarks = models.CharField(max_length=40, default=None)
    ActiveFlag = models.CharField(max_length=3, default=None)
    CreatedBy = models.CharField(max_length=15, default='A')
    UpdatedBy = models.CharField(max_length=15, default='A')
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class MstPatientPaymentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    RecordIDFK = models.ForeignKey(MstPatient, on_delete=models.RESTRICT)
    PatientID = models.CharField(max_length=11)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    PaymentType = models.CharField(max_length=15, default=None)
    PaymentMode = models.CharField(max_length=15, default='No mode', blank=True)
    InsuranceNo = models.CharField(max_length=20, default=None)
    InsuranceCompanyName = models.CharField(max_length=100, default=None)
    ActiveFlag = models.CharField(max_length=3, default=None)
    CreatedBy = models.CharField(max_length=15, default='A')
    UpdatedBy = models.CharField(max_length=15, default="A")
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)
