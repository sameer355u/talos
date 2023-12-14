from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages

from CustomAuth.utility import get_user_menu
from Patient.models.patient import MstPatient, MstPatientMedicalHistory, MstPatientContact, MstPatientPaymentDetails
from django.db import transaction
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage


@login_required(login_url='account_login')
# @allowed_group_users(allowed_group=['Admin'])
def index(request):
    if request.user.is_authenticated:
        return render(request, 'p_index.html')
    else:
        return redirect('account_login')


today = datetime.now().date()


def calculate_age(birthdate):
    delta = today - birthdate
    years = delta.days // 365
    return years


@login_required(login_url='account_login')
def patient_registration(request):
    if request.method == 'GET':
        data = get_user_menu(request)
        # MstPatientdata=MstPatient.objects.all()
        obj = list(MstPatient.objects
                   .select_related('mstpatientcontact__PatientIDFK')
                   .filter(ActiveFlag='A', UserIDFK=request.user)
                   .values('PatientID', 'FirstName', 'MiddleName', 'LastName', 'Gender', 'Age', 'BloodGroup',
                           'mstpatientcontact__PatientEmailId', 'AadharNo', 'MaritalStatus', 'SpouseName',
                           'mstpatientcontact__PatientContactNumber',
                           'Nationality', 'Address', 'City', 'State', 'Country', 'Pin',
                           'mstpatientcontact__AlternatNumber',
                           'mstpatientcontact__EmergencyContactName', 'mstpatientcontact__EmergencyContactNumber',
                           'mstpatientcontact__EmergencyContactRelation'))

        return render(request, 'patient_registration.html', {'obj': obj, 'data': data})
    else:
        fs = FileSystemStorage()
        # profilepic = request.FILES.get('selectedImageText',None)
        # profilepicsave=fs.save(profilepic.name, profilepic)

        DOB_str = request.POST.get('age', None)
        DOB = datetime.strptime(DOB_str, '%Y-%m-%d').date()
        age = calculate_age(DOB)

        preexistingcondition = request.POST.getlist('pretype'),
        description = request.POST.getlist('descrptn'),
        medicalrecordfile = request.FILES.getlist('medrec')
        for row in medicalrecordfile:
            print(row.name)
            print(row.size)
        remarks = request.POST.getlist('remarks')
        print(medicalrecordfile)
        try:
            with transaction.atomic():

                patient = MstPatient(
                    PatientID='P' + str(MstPatient.objects.all().count() + 1).zfill(9),
                    UserIDFK=request.user,
                    FirstName=request.POST.get('firstname', None),
                    MiddleName=request.POST.get('middlename', None),
                    LastName=request.POST.get('lastname', None),
                    City=request.POST.get('city', None),
                    State=request.POST.get('state', None),
                    Country=request.POST.get('country', None),
                    Pin=request.POST.get('pincode', None),
                    Gender=request.POST.get('gender', None),
                    BloodGroup=request.POST.get('patientbloodgroup', None),
                    Nationality=request.POST.get('nationality', None),
                    AadharNo=request.POST.get('aadhar', None),
                    MaritalStatus=request.POST.get('maritals', None),
                    SpouseName=request.POST.get('spousename', None),
                    Address=request.POST.get('address', None),
                    DOB=DOB,
                    Age=age,
                    ActiveFlag='A',
                    PatientProfileImage="WhatsApp Image 2023-11-11 at 12.33.04 PM.jpeg"

                )
                patient.save()
                print(patient.PatientProfileImage)
                PatientId = patient.PatientID

                contactdetails = MstPatientContact(
                    PatientContactNumber=request.POST.get('patcontactno', None),
                    AlternatNumber=request.POST.get('patalternateno', None),
                    PatientEmailId=request.POST.get('patemail', None),
                    EmergencyContactNumber=request.POST.get('emgcontact', None),
                    EmergencyContactName=request.POST.get('emgname', None),
                    EmergencyContactRelation=request.POST.get('emgcontactrelation', None),
                    ActiveFlag='A',
                    PatientID=PatientId,
                    UserIDFK=request.user,
                    RecordIDFK=patient

                )
                contactdetails.save()
                print(contactdetails)
                print(description)
                print(preexistingcondition)
                print(remarks)
                print(medicalrecordfile)

                for i in range(len(medicalrecordfile)):
                    if i < len(description[0]) and i < len(medicalrecordfile[0]) and i < len(remarks):
                        medicalrecordsave = fs.save(medicalrecordfile[i].name, medicalrecordfile[i])
                        medicalhistory = MstPatientMedicalHistory(
                            ActiveFlag='A',
                            PatientID=PatientId,
                            UserIDFK=request.user,
                            RecordIDFK=patient,
                            PreExistingCondition=preexistingcondition[0][i],
                            Description=description[0][i],
                            MedicalRecordFile=medicalrecordsave,
                            Remarks=remarks[i],
                            # id=MstPatientMedicalHistory.objects.all().count() + 1,
                        )
                        print(i)
                        medicalhistory.save()
                        print(medicalhistory, 'mh')

                paymentdetails = MstPatientPaymentDetails(
                    PatientID=PatientId,
                    PaymentType=request.POST.get('paymenttype', None),
                    PaymentMode=request.POST.get('paymentmode', None),
                    InsuranceCompanyName=request.POST.get('insurancename', None),
                    InsuranceNo=request.POST.get('insuranceno', None),
                    ActiveFlag='A',
                    UserIDFK=request.user,
                    RecordIDFK=patient

                )
                paymentdetails.save()
                print(patient.PatientProfileImage, patient.FirstName)
                messages.info(request, 'Registration Successful!')
                return redirect('patient_registration')
        except Exception as e:
            messages.warning(request, "Not Submitted", e)
            print('error occur', e)


@login_required(login_url='account_login')
def edit_patient_details(request):
    if request.method == 'POST':
        fullname = request.POST.get('mfullname').split()
        first_name = fullname[0] if fullname else ''
        middle_name = fullname[1] if len(fullname) > 1 else ''
        last_name = ' '.join(fullname[2:]) if len(fullname) > 2 else ''

        try:
            with transaction.atomic():
                PatientID = request.POST.get('patientid')
                MstPatient.objects.filter(PatientID=PatientID, ActiveFlag='A').update(ActiveFlag='I')

                patient = MstPatient(
                    PatientID=request.POST.get('patientid'),
                    FirstName=first_name,
                    MiddleName=middle_name,
                    LastName=last_name,
                    Gender=request.POST.get('mGender'),
                    Age=request.POST.get('mage'),
                    BloodGroup=request.POST.get('mbloodgroup'),
                    AadharNo=request.POST.get('maadhar'),
                    MaritalStatus=request.POST.get('mmaritalstatus'),
                    SpouseName=request.POST.get('mspousename'),
                    Nationality=request.POST.get('mnationality'),
                    City=request.POST.get('mcity'),
                    State=request.POST.get('mstate'),
                    Country=request.POST.get('mcountry'),
                    Pin=request.POST.get('mpin'),
                    Address=request.POST.get('maddress'),
                    UserIDFK=request.user,
                    ActiveFlag='A',
                    PatientProfileImage="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsr_agW6Kn1nq-MvsBdq0kQWV93PxRjXDEHw&usqp=CAU"

                )
                patient.save()

                MstPatientContact.objects.filter(PatientID=PatientID, ActiveFlag='A').update(ActiveFlag='I')

                contactdetails = MstPatientContact(
                    PatientID=request.POST.get('patientid'),
                    PatientContactNumber=request.POST.get('mcontactno'),
                    AlternatNumber=request.POST.get('malternateno'),
                    PatientEmailId=request.POST.get('memailid'),
                    EmergencyContactNumber=request.POST.get('emcontactno'),
                    EmergencyContactName=request.POST.get('memergencypersonname'),
                    EmergencyContactRelation=request.POST.get('mrelation'),
                    ActiveFlag='A',
                    UserIDFK=request.user,
                    RecordIDFK=patient
                )
                contactdetails.save()

                messages.info(request, 'Updated Successfully!')
                return redirect('patient_registration')

        except Exception as e:
            messages.warning(request, "Not Submitted edited ", e)
            print(f"An error occurred: {e}")
            return (request, {'error_message': str(e)})
