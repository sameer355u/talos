from CustomAuth.models import User, ProfessionalType
from django.db import models


class HealthProfessionalPersonalDetails(models.Model):
    HealthProfessionalPersonalDetailsIDPK = models.AutoField(primary_key=True)
    UserIdFK = models.ForeignKey(User, on_delete=models.RESTRICT)
    EmpID = models.CharField(max_length=10, default='EMP')
    EmailId = models.CharField(max_length=50, default=None)
    ProfileImage = models.ImageField(upload_to='healthprofessional/Image')
    AlternateContactNumber = models.BigIntegerField()
    MaritalStatus = models.CharField(max_length=20)
    Address = models.CharField(max_length=75, default=None)
    City = models.CharField(max_length=25, default=None)
    State = models.CharField(max_length=30, default=None)
    Country = models.CharField(max_length=30, default=None)
    Pin = models.IntegerField()
    SpouseName = models.CharField(max_length=20, default=None)
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_doctor(HealthProfessionalPersonalDetailsIDPK):
        return HealthProfessionalPersonalDetails.objects.get(HealthProfessionalPersonalDetailsIDPK=HealthProfessionalPersonalDetailsIDPK)

    @staticmethod
    def get_doctor_id(UserIDFK):
        return HealthProfessionalPersonalDetails.objects.get(UserIDFK=UserIDFK)

    @staticmethod
    def get_doctors_list():
        return HealthProfessionalPersonalDetails.objects.all()


class HealthProfessionalEducationDetails(models.Model):
    HealthProfessionalEducationIDPK = models.AutoField(primary_key=True)
    EmpID = models.CharField(max_length=10, default='EMP')
    QualificationType = models.CharField(max_length=20)
    QualificationName = models.CharField(max_length=50)
    CurrentStatus = models.CharField(max_length=30)
    PassingYear = models.IntegerField()
    CollegeIDFK = models.IntegerField()
    UniversityIDFK = models.IntegerField()
    ActiveFlag = models.CharField(max_length=3, default=True)
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_educational_detail_by_EmpID(EmpID):
        return HealthProfessionalEducationDetails.objects.get(EmpID=EmpID)


class HealthProfessionalExperienceDetails(models.Model):
    HealthProfessionalExperienceIDPK = models.AutoField(primary_key=True)
    EmpID = models.CharField(max_length=10, default='EMP')
    MedicalInstituteName = models.CharField(max_length=50)
    RoleName = models.CharField(max_length=20)
    ExperienceYears = models.IntegerField()
    JobDescription = models.CharField(max_length=40)
    StartDate = models.DateField()
    EndDate = models.DateField()
    ActiveFlag = models.CharField(max_length=3, default=True)
    Status = models.CharField(max_length=10, default='Pending')
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_experience_detail_by_EmpID(EmpID):
        return HealthProfessionalEducationDetails.objects.get(EmpID=EmpID)


class HealthProfessionalCertificationDetails(models.Model):
    HealthProfessionalCertificateIDPK = models.AutoField(primary_key=True)
    EmpID = models.CharField(max_length=10, default='EMP')
    CertificateName = models.CharField(max_length=50)
    UploadCertificateLink = models.FileField(upload_to='healthprofessional')
    IssueDate = models.DateField()
    ExpiryDate = models.DateField()
    ActiveFlag = models.CharField(max_length=3, default=True)
    Status = models.CharField(max_length=10, default='Pending')
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_certification_detail_by_EmpID(EmpID):
        return HealthProfessionalEducationDetails.objects.get(EmpID=EmpID)


class HealthProfessionalDocumentLinks(models.Model):
    HealthProfessionalDocumentLinksIDPK = models.AutoField(primary_key=True)
    EmpID = models.CharField(max_length=10, default='EMP')
    DocumentType = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    DocumentLink = models.FileField(upload_to='healthprofessional')
    Remarks = models.CharField(max_length=50)
    ActiveFlag = models.CharField(max_length=3, default=True)
    Status = models.CharField(max_length=10, default='Pending')
    CreatedBy = models.CharField(max_length=15)
    UpdatedBy = models.CharField(max_length=15)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateTimeField(auto_now=True)


class HealthProfessionalBankDetails(models.Model):
    HealthProfessionalBankDetailsIDPK = models.AutoField(primary_key=True)
    EmpID = models.CharField(max_length=10, default='EMP')
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

class MstHealthProfessional(models.Model):
    MstHealthProfessionalIDPK= models.AutoField(primary_key=True)
    EmpID=models.CharField(max_length=10,default='EMP')
    EmpEmail=models.CharField(max_length=50,default=None)
    EmpPhoneNumber	=models.BigIntegerField()
    DateOfBirth=models.DateField()
    UserIDFK = models.ForeignKey(User, on_delete=models.RESTRICT, default=User)
    FirstName=models.CharField(max_length=20)
    MiddleName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    Nationality=models.CharField(max_length=15,default=None)
    AadharNo=models.BigIntegerField(default=78)
    Gender=models.CharField(max_length=9)
    BloodGroup=models.CharField(max_length=4,default=None)
    EmployeeStatus=models.CharField(max_length=20,default='Applicant')
    ApprovalStatus=models.CharField(max_length=20,default='Pending')
    ProfessionalTypeIdFK=models.ForeignKey(ProfessionalType,on_delete=models.RESTRICT,default=ProfessionalType)
    Designation	=models.CharField(max_length=30,default='Applicant')
    EmpStartDate=models.DateField(auto_now_add=True)
    EmpEndDate	=models.DateField(blank=True,null=True)
    ActiveFlag =models.CharField(max_length=2,default='A')
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
