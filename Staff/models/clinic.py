from CustomAuth.models import User
from django.db import models


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    clinic_code = models.CharField(max_length=50, unique=True)
    clinic_name = models.CharField(max_length=50, unique=True)
    clinic_type = models.CharField(max_length=50)
    address_Line1 = models.CharField(max_length=100)
    address_Line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    PinCode = models.IntegerField()
    GST_IN = models.CharField(max_length=30, unique=True)
    reg_No = models.CharField(max_length=30, unique=True)
    license_No = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    update_time = models.TimeField(auto_now=True)

    @staticmethod
    def get_clinic_id():
        return Clinic.objects.get(clinic_id=1)

    def __str__(self):
        return self.clinic_name


class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.RESTRICT)
    lab_name = models.CharField(max_length=50, unique=True)
    lab_desc = models.CharField(max_length=400)
    address_Line1 = models.CharField(max_length=100)
    address_Line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    PinCode = models.IntegerField()
    GST_IN = models.CharField(max_length=30, unique=True)
    reg_No = models.CharField(max_length=30, unique=True)
    license_No = models.CharField(max_length=30, unique=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    update_time = models.TimeField(auto_now=True)


class LabTest(models.Model):
    labTest_id = models.AutoField(primary_key=True)
    lab = models.ForeignKey(Lab, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    charge = models.FloatField()
    Tax = models.FloatField()
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


class LabReportParameter(models.Model):
    parameter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lab_test = models.ForeignKey(LabTest, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    create_time = models.TimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    update_time = models.TimeField(auto_now=True)
