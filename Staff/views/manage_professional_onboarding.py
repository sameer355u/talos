from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import date,datetime
from django.db import transaction
from django.contrib import messages
from django.db.models import Q
from CustomAuth.models import User, ProfessionalType
from django.core.files.storage import FileSystemStorage
from Staff.models.professional_Onboarding import HealthProfessionalBankDetails,HealthProfessionalCertificationDetails,HealthProfessionalDocumentLinks,HealthProfessionalEducationDetails,HealthProfessionalExperienceDetails,HealthProfessionalPersonalDetails,MstCollege,MstUniversity,MstFlag,MstHealthProfessional



def medical_professional_onboarding(request):
    if request.method=='GET':

      context={'specializationtype':MstFlag.objects.filter(Q(FlagName='SpecializationType')|Q(FlagName='NurseType')).values('FlagID','FlagValue'),
               'doc_type':MstFlag.objects.filter(FlagName='HealthProfessionalDocumentType'),'cert_type':MstFlag.objects.filter(FlagName='Certifications'),
               'collegelist':MstCollege.objects.all(), 'universitylist':MstUniversity.objects.all(),'educationtype':MstFlag.objects.filter(FlagName='EducationType') }
      return render(request, 'Medical-Professional-Onboarding.html',context)
    else:

        try:

            # profilepic=request.FILES.get('ImageInput',None)
            # profilepicsave=fs.save(profilepic.name,profilepic)
            DOB=request.POST.get('dob',None)
            parsed_date = datetime.strptime(DOB, "%B %d, %Y")
            formatted_date = parsed_date.strftime("%Y-%m-%d")

            qualtype=request.POST.getlist('qualification',None)
            qualname=request.POST.getlist('qualificationname',None)
            curstatus=request.POST.getlist('currentstatus',None)
            year=request.POST.getlist('passingyear',None)
            collegename=request.POST.getlist('institute',None)
            univ=request.POST.getlist('university',None)



            medinst=request.POST.getlist('institutename',None)
            rolename=request.POST.getlist('role',None)
            expdetail=request.POST.getlist('experien',None)
            jobdescription=request.POST.getlist('jobdesc',None)
            startd=request.POST.getlist('stdate',None)
            endd=request.POST.getlist('endate',None)


            certificname=request.POST.getlist('certtype',None)
            certupload=request.FILES.getlist('uploadcert',None)
            issue=request.POST.getlist('issued',None)
            expiry=request.POST.getlist('expiryd',None)


            doctype=request.POST.getlist('doctype',None)
            docname=request.POST.getlist('docname',None)
            remarks=request.POST.getlist('remarks',None)
            uploaddoc=request.FILES.getlist('uploaddoc',None)



            with transaction.atomic():
              fs=FileSystemStorage()

              healthprofessional=MstHealthProfessional(
                 UserIDFK=request.user,
                 EmpEmail=request.user.email,
                 EmpPhoneNumber=request.POST.get('mob',None),
                 FirstName=request.POST.get('firstname'),
                 MiddleName=request.POST.get('middlename', None),
                 LastName=request.POST.get('lastname'),
                 DateOfBirth=formatted_date,
                 Gender=request.POST.get('gender'),
                 BloodGroup=request.POST.get('patientbloodgroup'),
                 Nationality=request.POST.get('nationality'),
                 AadharNo=request.POST.get('aadhar'),
                 ProfessionalTypeIdFK=request.user.profession,
                 ActiveFlag='A',
                 EmpID='EMP00001'
              )
              healthprofessional.save()

              personaldetails=HealthProfessionalPersonalDetails(

                  EmailId=request.POST.get('persemail'),
                  AlternateContactNumber=request.POST.get('alternateno'),
                  MaritalStatus=request.POST.get('maritals', None),
                  SpouseName=request.POST.get('spousename', None),
                  Address=request.POST.get('address'),
                  City=request.POST.get('city'),
                  State=request.POST.get('state'),
                  Country=request.POST.get('country'),
                  Pin=request.POST.get('pincode'),
                  ActiveFlag='A',
                  ProfileImage='whatsapp',
                  EmpID='EMP00001'
                 )
              personaldetails.save()

              for i in range(len(qualtype)):
                  educationdetails=HealthProfessionalEducationDetails(

                    QualificationType=qualtype[i],
                    QualificationName=qualname[i],
                    CurrentStatus=curstatus[i],
                    PassingYear=year[i],
                    CollegeIDFK=collegename[i],
                    UniversityIDFK=univ[i],
                    ActiveFlag='A',
                    EmpID='EMP00001'
                  )
                  educationdetails.save()


              for i in range(len(rolename)):
                    experiencedetails=HealthProfessionalExperienceDetails(

                      MedicalInstituteName=medinst[i],
                      RoleName=rolename[i],
                      ExperienceYears=expdetail[i],
                      JobDescription=jobdescription[i],
                      StartDate=startd[i],
                      EndDate=endd[i],
                      ActiveFlag='A',
                      EmpID='EMP00001'
                    )
                    experiencedetails.save()

              bankdetails=HealthProfessionalBankDetails(

                AccountHolderName=request.POST.get('holdername'),
                AccountType=request.POST.get('accounttype'),
                AccountNumber=request.POST.get('accnumber'),
                IFSCCode=request.POST.get('ifsccode'),
                BankName=request.POST.get('bankname'),
                BranchName=request.POST.get('branchname'),

                ActiveFlag='A',
                EmpID='EMP00001'
              )
              bankdetails.save()

              for i in range(len(uploaddoc)):

                uploaddocsave=fs.save(uploaddoc[i].name,uploaddoc[i])

                documentdetails=HealthProfessionalDocumentLinks(

                    DocumentType=doctype[i],
                    DocumentName=docname[i],
                    DocumentLink=uploaddocsave,
                    Remarks=remarks[i],
                    ActiveFlag='A',
                    EmpID='EMP00001'
                )
                documentdetails.save()

              for i in range(len(certupload)):
                  # if i < len(certificname) and i < len(certupload) and i < len(issue):

                    certificnamesave=fs.save(certupload[i].name,certupload[i])

                    certificationdetails=HealthProfessionalCertificationDetails(

                        CertificateName=certificname[i],
                        UploadCertificateLink=certificnamesave,
                        IssueDate=issue[i],
                        ExpiryDate=expiry[i],
                        ActiveFlag='A',
                        EmpID='EMP00001'
                    )
                    certificationdetails.save()





            messages.info(request,'Onboarding request has been made! Wait for Approval')
            return redirect('medical_professional_onboarding')
            # redirect('')
        except Exception as e:

          messages.warning(request,{'Not Submitted': str(e)})
          return redirect('medical_professional_onboarding')
