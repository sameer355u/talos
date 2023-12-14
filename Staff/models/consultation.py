from django.db import models
from Patient.models.appointment import Appointment

class Vitals(models.Model):
    vitals_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    systolic = models.IntegerField(default=None)
    diastolic = models.IntegerField(default=None)
    temperature = models.FloatField()
    pulse = models.IntegerField()
    respiratory_rate = models.IntegerField()
    random_blood_sugar = models.FloatField()
    spo2 = models.IntegerField()
    level_of_consciousness = models.CharField(max_length=20)
    pupillary_response = models.CharField(max_length=20)

class Symptoms(models.Model):
    symptoms_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    symptoms = models.TextField()

    def __str__(self):
        return f"Symptoms of {self.appointment} - ID: {self.symptoms_id}"

class PreExisting(models.Model):
    preexisting_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    preexisting_info = models.TextField()

    def __str__(self):
        return f"Pre-Existing Information of {self.appointment} - ID: {self.preexisting_id}"


class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    clinical_notes = models.TextField()
    diagnosis = models.TextField()

    def __str__(self):
        return f"Pre-Existing Information of {self.appointment} - ID: {self.diagnosis_id}"


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255)
    document_type = models.CharField(max_length=50)
    description = models.TextField()
    remark = models.TextField()
    document_file = models.FileField(upload_to='uploads/documents')


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    lab_investigation = models.TextField(max_length=255)
    advice = models.TextField()
    follow_up_date = models.DateField()
    remark = models.TextField()
    rx_data = models.TextField()

