# Generated by Django 4.2.7 on 2023-12-06 18:27

import CustomAuth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CustomAuth', '0001_initial'),
        ('Patient', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('clinic_id', models.AutoField(primary_key=True, serialize=False)),
                ('clinic_code', models.CharField(max_length=50, unique=True)),
                ('clinic_name', models.CharField(max_length=50, unique=True)),
                ('clinic_type', models.CharField(max_length=50)),
                ('address_Line1', models.CharField(max_length=100)),
                ('address_Line2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('PinCode', models.IntegerField()),
                ('GST_IN', models.CharField(max_length=30, unique=True)),
                ('reg_No', models.CharField(max_length=30, unique=True)),
                ('license_No', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('update_time', models.TimeField(auto_now=True)),
                ('user', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalBankDetails',
            fields=[
                ('HealthProfessionalBankDetailsIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('AccountType', models.CharField(max_length=20)),
                ('AccountHolderName', models.CharField(max_length=35)),
                ('AccountNumber', models.BigIntegerField()),
                ('IFSCCode', models.CharField(max_length=11)),
                ('BankName', models.CharField(max_length=50)),
                ('BranchName', models.CharField(max_length=20)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalCertificationDetails',
            fields=[
                ('HealthProfessionalCertificateIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('CertificateName', models.CharField(max_length=50)),
                ('UploadCertificateLink', models.FileField(upload_to='healthprofessional')),
                ('IssueDate', models.DateField()),
                ('ExpiryDate', models.DateField()),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('Status', models.CharField(default='Pending', max_length=10)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalDocumentLinks',
            fields=[
                ('HealthProfessionalDocumentLinksIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('DocumentType', models.CharField(max_length=50)),
                ('DocumentName', models.CharField(max_length=50)),
                ('DocumentLink', models.FileField(upload_to='healthprofessional')),
                ('Remarks', models.CharField(max_length=50)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('Status', models.CharField(default='Pending', max_length=10)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalEducationDetails',
            fields=[
                ('HealthProfessionalEducationIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('QualificationType', models.CharField(max_length=20)),
                ('QualificationName', models.CharField(max_length=50)),
                ('CurrentStatus', models.CharField(max_length=30)),
                ('PassingYear', models.IntegerField()),
                ('CollegeIDFK', models.IntegerField()),
                ('UniversityIDFK', models.IntegerField()),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalExperienceDetails',
            fields=[
                ('HealthProfessionalExperienceIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('MedicalInstituteName', models.CharField(max_length=50)),
                ('RoleName', models.CharField(max_length=20)),
                ('ExperienceYears', models.IntegerField()),
                ('JobDescription', models.CharField(max_length=40)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('Status', models.CharField(default='Pending', max_length=10)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthProfessionalPersonalDetails',
            fields=[
                ('HealthProfessionalPersonalDetailsIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('EmailId', models.CharField(default=None, max_length=50)),
                ('ProfileImage', models.ImageField(upload_to='healthprofessional/Image')),
                ('AlternateContactNumber', models.BigIntegerField()),
                ('MaritalStatus', models.CharField(max_length=20)),
                ('Address', models.CharField(default=None, max_length=75)),
                ('City', models.CharField(default=None, max_length=25)),
                ('State', models.CharField(default=None, max_length=30)),
                ('Country', models.CharField(default=None, max_length=30)),
                ('Pin', models.IntegerField()),
                ('SpouseName', models.CharField(default=None, max_length=20)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=50, unique=True)),
                ('lab_desc', models.CharField(max_length=400)),
                ('address_Line1', models.CharField(max_length=100)),
                ('address_Line2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('PinCode', models.IntegerField()),
                ('GST_IN', models.CharField(max_length=30, unique=True)),
                ('reg_No', models.CharField(max_length=30, unique=True)),
                ('license_No', models.CharField(max_length=30, unique=True)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('update_time', models.TimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.clinic')),
                ('user', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MstCollege',
            fields=[
                ('CollegeIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('CollegeName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MstFlag',
            fields=[
                ('FlagID', models.AutoField(primary_key=True, serialize=False)),
                ('FlagName', models.CharField(max_length=100)),
                ('FlagValue', models.CharField(max_length=100)),
                ('FlagDesc', models.CharField(max_length=100)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MstUniversity',
            fields=[
                ('UniversityIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('UniversityName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ActiveFlag', models.CharField(default=True, max_length=3)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblDoctorSchedule',
            fields=[
                ('DoctorScheduleIdPK', models.AutoField(primary_key=True, serialize=False)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('SlotDuration', models.IntegerField()),
                ('Day', models.CharField(max_length=10)),
                ('StartTime', models.TimeField()),
                ('NoofSlots', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('CreatedBy', models.CharField(max_length=8)),
                ('UpdatedBy', models.CharField(max_length=8)),
                ('CreationDateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdationDateTime', models.DateTimeField(auto_now=True)),
                ('ClinicIdFK', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.clinic')),
                ('DoctorIdFK', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.healthprofessionalpersonaldetails')),
                ('UserIdFK', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('vitals_id', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('systolic', models.IntegerField(default=None)),
                ('diastolic', models.IntegerField(default=None)),
                ('temperature', models.FloatField()),
                ('pulse', models.IntegerField()),
                ('respiratory_rate', models.IntegerField()),
                ('random_blood_sugar', models.FloatField()),
                ('spo2', models.IntegerField()),
                ('level_of_consciousness', models.CharField(max_length=20)),
                ('pupillary_response', models.CharField(max_length=20)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='TblDoctorSlot',
            fields=[
                ('DoctorSlotIdPK', models.AutoField(primary_key=True, serialize=False)),
                ('SlotDate', models.DateField()),
                ('Day', models.CharField(max_length=10)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
                ('Status', models.CharField(max_length=10)),
                ('AppointmentIdFK', models.IntegerField()),
                ('CreatedBy', models.CharField(max_length=8)),
                ('UpdatedBy', models.CharField(max_length=8)),
                ('CreationDateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdationDateTime', models.DateTimeField(auto_now=True)),
                ('ClinicIdFK', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.clinic')),
                ('DoctorIdFK', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.healthprofessionalpersonaldetails')),
                ('DoctorScheduleIdFK', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.tbldoctorschedule')),
                ('UserIdFK', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('symptoms_id', models.AutoField(primary_key=True, serialize=False)),
                ('symptoms', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_investigation', models.TextField(max_length=255)),
                ('advice', models.TextField()),
                ('follow_up_date', models.DateField()),
                ('remark', models.TextField()),
                ('rx_data', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='PreExisting',
            fields=[
                ('preexisting_id', models.AutoField(primary_key=True, serialize=False)),
                ('preexisting_info', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='MstHealthProfessional',
            fields=[
                ('MstHealthProfessionalIDPK', models.AutoField(primary_key=True, serialize=False)),
                ('EmpID', models.CharField(default='EMP', max_length=10)),
                ('EmpEmail', models.CharField(default=None, max_length=50)),
                ('EmpPhoneNumber', models.BigIntegerField()),
                ('DateOfBirth', models.DateField()),
                ('FirstName', models.CharField(max_length=20)),
                ('MiddleName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Nationality', models.CharField(default=None, max_length=15)),
                ('AadharNo', models.BigIntegerField(default=78)),
                ('Gender', models.CharField(max_length=9)),
                ('BloodGroup', models.CharField(default=None, max_length=4)),
                ('EmployeeStatus', models.CharField(default='Applicant', max_length=20)),
                ('ApprovalStatus', models.CharField(default='Pending', max_length=20)),
                ('Designation', models.CharField(default='Applicant', max_length=30)),
                ('EmpStartDate', models.DateField(auto_now_add=True)),
                ('EmpEndDate', models.DateField(blank=True, null=True)),
                ('ActiveFlag', models.CharField(default='A', max_length=2)),
                ('CreatedBy', models.CharField(max_length=15)),
                ('UpdatedBy', models.CharField(max_length=15)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('UpdationDate', models.DateTimeField(auto_now=True)),
                ('ProfessionalTypeIdFK', models.ForeignKey(default=CustomAuth.models.ProfessionalType, on_delete=django.db.models.deletion.RESTRICT, to='CustomAuth.professionaltype')),
                ('UserIDFK', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('labTest_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('charge', models.FloatField()),
                ('Tax', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.lab')),
            ],
        ),
        migrations.CreateModel(
            name='LabReportParameter',
            fields=[
                ('parameter_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('create_time', models.TimeField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('update_time', models.TimeField(auto_now=True)),
                ('lab_test', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Staff.labtest')),
                ('user', models.ForeignKey(default=CustomAuth.models.User, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_name', models.CharField(max_length=255)),
                ('document_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('remark', models.TextField()),
                ('document_file', models.FileField(upload_to='uploads/documents')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('clinical_notes', models.TextField()),
                ('diagnosis', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.appointment')),
            ],
        ),
    ]
