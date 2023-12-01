from CustomAuth.models import User, ProfessionalType
from django.db import models


class HealthProfessionalPersonalDetails(models.Model):
    HealthProfessionalIDPK = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=35)
    # ProfessionalTypeID = models.ForeignKey(ProfessionalType, on_delete=models.RESTRICT)
    ProfessionalProfilePic = models.ImageField(upload_to='staff/profile_picture')
    ContactNumber = models.BigIntegerField()
    DateOfBirth = models.DateField()
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    GenderType = [('M', 'Male'), ('F', 'female'), ('O', 'Others')]
    Gender = models.CharField(max_length=9, choices=GenderType)
    BloodGroup = models.CharField(max_length=4, default=None)
    Nationality = models.CharField(max_length=15, default=None)
    AadharNo = models.BigIntegerField(default=78, unique=True)
    MaritalStatustype = [('U', 'Unmarried'), ('Mrd', 'Married'), ('D', 'Divorcee'), ('W', 'Widow')]
    MaritalStatus = models.CharField(max_length=15, choices=MaritalStatustype)
    Address = models.CharField(max_length=75, default=None)
    City = models.CharField(max_length=25, default=None)
    State = models.CharField(max_length=30, default=None)
    Country = models.CharField(max_length=30, default=None)
    Pin = models.IntegerField()
    SpouseName = models.CharField(max_length=20, default=None)
    ActiveFlag = models.CharField(max_length=3, default=True)
    Status = models.CharField(max_length=10)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_doctor(HealthProfessionalIDPK):
        return HealthProfessionalPersonalDetails.objects.get(HealthProfessionalIDPK=HealthProfessionalIDPK)

    @staticmethod
    def get_doctor_id(UserIDFK):
        return HealthProfessionalPersonalDetails.objects.get(UserIDFK=UserIDFK)

    @staticmethod
    def get_doctors_list():
        return HealthProfessionalPersonalDetails.objects.all()


class HealthProfessionalEducationDetails(models.Model):
    HealthProfessionalEducationIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    QualificationName = models.CharField(max_length=30)
    CurrentStatus = models.CharField(max_length=20)
    PassingYear = models.IntegerField()
    InstituteName = models.CharField(max_length=75, blank=True)
    UniversityName = models.CharField(max_length=75, blank=True)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_educational_detail_by_staff_id(HealthProfessionalIDFK):
        return HealthProfessionalEducationDetails.objects.get(HealthProfessionalIDFK=HealthProfessionalIDFK)


class HealthProfessionalSpecializationDetails(models.Model):
    HealthProfessionalSpecializationIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    SpecializationType = models.CharField(max_length=30)
    # Fellowship=models.CharField(max_length=50,blank=True)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_specialization_detail_by_staff_id(HealthProfessionalIDFK):
        return HealthProfessionalEducationDetails.objects.get(HealthProfessionalIDFK=HealthProfessionalIDFK)


class HealthProfessionalExperienceDetails(models.Model):
    HealthProfessionalExperienceIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    MedicalInstituteName = models.CharField(max_length=50)
    RoleName = models.CharField(max_length=20)
    ExperienceYears = models.IntegerField()
    JobDescription = models.CharField(max_length=40)
    StartDate = models.DateField()
    EndDate = models.DateField()
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_experience_detail_by_staff_id(HealthProfessionalIDFK):
        return HealthProfessionalEducationDetails.objects.get(HealthProfessionalIDFK=HealthProfessionalIDFK)


class HealthProfessionalCertificationDetails(models.Model):
    HealthProfessionalCertificateIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)
    CertificateName = models.CharField(max_length=25)
    UploadCertificateLink = models.FileField(upload_to='staff/Health_Professional_Documents')
    IssueDate = models.DateField()
    ExpiryDate = models.DateField()
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_certification_detail_by_staff_id(HealthProfessionalIDFK):
        return HealthProfessionalEducationDetails.objects.get(HealthProfessionalIDFK=HealthProfessionalIDFK)


class HealthProfessionalDocumentLinks(models.Model):
    HealthProfessionalDocumentLinksIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)

    DocumentType = models.CharField(max_length=15)
    DocumentName = models.CharField(max_length=20)
    DocumentLink = models.FileField(upload_to='staff/Health_Professional_Documents')
    Remarks = models.CharField(max_length=30)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class HealthProfessionalBankDetails(models.Model):
    HealthProfessionalBankDetailsIDPK = models.AutoField(primary_key=True)
    HealthProfessionalIDFK = models.ForeignKey(HealthProfessionalPersonalDetails, on_delete=models.RESTRICT)

    AccountType = models.CharField(max_length=20)
    AccountHolderName = models.CharField(max_length=35)
    AccountNumber = models.BigIntegerField()
    IFSCCode = models.CharField(max_length=11)
    BankName = models.CharField(max_length=50)
    BranchName = models.CharField(max_length=20)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class MstUniversity(models.Model):
    UniversityIDPK = models.AutoField(primary_key=True)
    UniversityName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class MstCollege(models.Model):
    CollegeIDPK = models.AutoField(primary_key=True)
    CollegeName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class MstFlag(models.Model):
    FlagID = models.AutoField(primary_key=True)
    FlagName = models.CharField(max_length=100)
    FlagValue = models.CharField(max_length=100)
    FlagDesc = models.CharField(max_length=100)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)
