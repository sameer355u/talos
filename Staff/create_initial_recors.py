from django.contrib.auth.hashers import make_password
from CustomAuth.models import ProfessionalType, User
from allauth.socialaccount.models import SocialApp
from CustomAuth.models_grp_role import MstMenuItem
from Staff.models.professional_Onboarding import MstFlag


def create_admin():
    try:
        professions = ['Admin', 'Patient', 'Doctor', 'Front-Desk']
        for i in professions:
            po = ProfessionalType(name=i)
            po.save()
        p = ProfessionalType.objects.get(name='Admin')

        phone = 8888888888
        pa = 'adminadmin'
        password = make_password(pa)
        email = 'admin@dnits.com'

        user = User(profession=p, phone=phone, password=password, email=email, is_superuser=True, is_staff=True)
        user.save()

        s = SocialApp(
            provider='google',
            name='Google SSO',
            client_id='341096323111-gls9q9l55dthp0bb1rne0kl3o3q4fah5.apps.googleusercontent.com',
            secret='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',
            settings='{}')
        s.save()
    except:
        pass


def insert_mst_records(request):
    # ######## MST-Flag Entries: ------
    mst_data = [[1, 'SpecializationType', ' Anaesthesia', 'Anaesthesia', 'A'],
                [2, 'SpecializationType', ' BAMS', 'BAMS', 'A'],
                [3, 'SpecializationType', 'Cardiology', 'Cardiology', 'A'],
                [4, 'SpecializationType', 'Dentist/BDS', 'Dentist/BDS', 'A'],
                [5, 'SpecializationType', 'Diabetologist', 'Diabetologist', 'A'],
                [6, 'SpecializationType', 'Dietician', 'Dietician', 'A'],
                [7, 'SpecializationType', 'Endocrinology', 'Endocrinology', 'A'],
                [8, 'SpecializationType', 'ENT', 'ENT', 'A'],
                [9, 'SpecializationType', 'Gastroenterologist', 'Gastroenterologist', 'A'],
                [10, 'EducationType', 'X', 'X', 'A'],
                [11, 'Certifications', 'License', 'License', 'A'],
                [12, 'HealthProfessionalDocumentType', 'State Medical Council Registration', 'Registration', 'A'],
                [13, 'HealthProfessionalDocumentType', 'Healthcare Professional Registry', 'HPR', 'A'],
                [14, 'HealthProfessionalDocumentType', 'No Objection Certificate', 'No Objection Certificate', 'A'],
                [15, 'Certifications', 'Internship Completion Certificate', 'Internship Certificate', 'A'],
                [16, 'HealthProfessionalDocumentType', 'Aadhar', 'Aadhar', 'A'],
                [17, 'HealthProfessionalDocumentType', 'Marksheet', 'MBBS Degree', 'A'],
                [18, 'HealthProfessionalDocumentType', 'Digital Signature', 'Digital Signature', 'A'],
                [19, 'HealthProfessionalDocumentType', 'PAN Card', 'PAN Card', 'A'],
                [20, 'HealthProfessionalDocumentType', 'Others', 'Others', 'A'],
                [21, 'NurseType', 'Registered Auxilliary Nurse Midwife', 'Registered Auxilliary Nurse Midwife', 'A'],
                [22, 'NurseType', 'Registered Nurse and Registered Midwife', 'Registered Nurse and Registered Midwife',
                 'A'],
                [23, 'NurseType', 'Registered Nurse', 'Registered Nurse', 'A'],
                [24, 'NurseType', 'Registered Lady Health Visitor', 'Registered Lady Health Visitor', 'A'],
                [25, 'SpecializationType', 'General surgeon', 'General surgeon', 'A'],
                [26, 'SpecializationType', 'MDS', 'MDS', 'A'],
                [27, 'SpecializationType', 'Medicine', 'Medicine', 'A'],
                [28, 'SpecializationType', 'Neurology', 'Neurology', 'A'],
                [29, 'SpecializationType', 'Obstetrician/ Gynaecologist', 'Obstetrician/ Gynaecologist', 'A'],
                [30, 'SpecializationType', 'Ophthalmology', 'Ophthalmology', 'A'],
                [31, 'SpecializationType', 'Paediatrics', 'Paediatrics', 'A'],
                [32, 'SpecializationType', 'Psychiatry', 'Psychiatry', 'A'],
                [33, 'SpecializationType', 'Psychologist', 'Psychologist', 'A'],
                [34, 'SpecializationType', 'Pulmonology', 'Pulmonology', 'A'],
                [35, 'SpecializationType', 'Rheumatologist/Immunologist', 'Rheumatologist/Immunologist', 'A'],
                [36, 'SpecializationType', 'Geriatric medicine', 'Geriatric medicine', 'A'],
                [37, 'SpecializationType', 'Urologist', 'Urologist', 'A'],
                [38, 'SpecializationType', 'Paediatric endocrinologist', 'Paediatric endocrinologist', 'A'],
                [39, 'SpecializationType', 'Oncologist', 'Oncologist', 'A'],
                [40, 'SpecializationType', 'Physiotherapist', 'Physiotherapist', 'A'],
                [41, 'SpecializationType', 'MD ayurveda', 'MD ayurveda', 'A'],
                [42, 'SpecializationType', 'IVF specialist', 'IVF specialist', 'A'],
                [43, 'SpecializationType', 'Emergency medicine', 'Emergency medicine', 'A'],
                [44, 'SpecializationType', 'Haematologist', 'Haematologist', 'A'],
                [45, 'SpecializationType', 'Orthopaedician', 'Orthopaedician', 'A'],
                [46, 'SpecializationType', 'General physician', 'General physician', 'A'],
                [47, 'EducationType', 'XII', 'XII', 'A'],
                [48, 'EducationType', 'UG', 'UG', 'A'],
                [49, 'EducationType', 'PG', 'PG', 'A'],
                [50, 'EducationType', 'Others', 'Others', 'A'],
                [51, 'Certifications', 'Others', 'Others', 'A']]

    for i in range(len(mst_data)):
        print(f'{i} : ', mst_data[i])
        mst_flag = MstFlag(FlagID=mst_data[i][0],
                           FlagName=mst_data[i][1],
                           FlagValue=mst_data[i][2],
                           FlagDesc=mst_data[i][3],
                           ActiveFlag='A',
                           CreatedBy=request.user.id,
                           UpdatedBy=request.user.id, )
        try:
            mst_flag.save()
        except:
            return None


def insert_menu_items():
    menu_item_list = [[1, 'Registration', '', 1, 1],
                      [2, 'PatientRegistration', '', 1, 1],
                      [3, 'Appointments', '', 3, 1],
                      [4, 'BookAppointment', '', 3, 1],
                      [5, 'RescheduleAppointment', '', 3, 1],
                      [6, 'CancelAppointment', '', 3, 1],
                      [7, 'BookHomeCareServices', '', 3, 1],
                      [8, 'BookTherapy', '', 3, 1],
                      [9, 'BookHospitalReferral', '', 3, 1],
                      [10, 'Payment', '', 10, 1],
                      [11, 'Consultation', '', 10, 1],
                      [12, 'Pathology', '', 10, 1],
                      [13, 'Procedure', '', 10, 1],
                      [14, 'Pharmacy', '', 10, 1],
                      [15, 'HomeCare', '', 10, 1],
                      [16, 'Others', '', 10, 1],
                      [17, 'Consultation', '', 17, 1],
                      [18, 'PreExamination', '', 17, 1],
                      [19, 'Write Prescription', '', 17, 1],
                      [20, 'ConductLabTest', '', 17, 1],
                      [21, 'GenerateLabReports', '', 17, 1],
                      [22, 'ConductProcedure', '', 17, 1],
                      [23, 'GenerateProcedurePrescription', '', 17, 1],
                      [24, 'ConductTherapySession', '', 17, 1],
                      [25, 'History', '', 25, 1],
                      [26, 'ViewPrescription', '', 25, 1],
                      [27, 'ViewReports', '', 25, 1],
                      [28, 'ViewProcedureNotes', '', 25, 1],
                      [29, 'ViewTherapyNotes', '', 25, 1],
                      [30, 'ViewInvoices', '', 25, 1],
                      [31, 'MasterScreens', '', 31, 1],
                      [32, 'FranchiseClinicStatus', '', 31, 1],
                      [33, 'FranchiseType', '', 31, 1],
                      [34, 'ClinicType', '', 31, 1],
                      [35, 'ClinicCentreType', '', 31, 1],
                      [36, 'ClinicCentreSubType', '', 31, 1],
                      [37, 'ClinicCentreMode', '', 31, 1],
                      [38, 'AppointmentBookingType', '', 31, 1],
                      [39, 'ConsultationType', '', 31, 1],
                      [40, 'AppointmentBookingStatusType', '', 31, 1],
                      [41, 'SlotStatusType', '', 31, 1],
                      [42, 'PaymentStatus', '', 31, 1],
                      [43, 'PaymentSourceType', '', 31, 1],
                      [44, 'PaymentType', '', 31, 1],
                      [45, 'WalletPaymentType', '', 31, 1],
                      [46, 'ProcedureType', '', 31, 1],
                      [47, 'SurgicalProcedureType', '', 31, 1],
                      [48, 'NonSurgicalProcedureType', '', 31, 1],
                      [49, 'LeaveType', '', 31, 1],
                      [50, 'LeaveStatus', '', 31, 1],
                      [51, 'HealthProfessionalDocumentType', '', 31, 1],
                      [52, 'DocumentType', '', 31, 1],
                      [53, 'PathologyLabType', '', 31, 1],
                      [54, 'ProcedureCentreType', '', 31, 1],
                      [55, 'TherapyCentreType', '', 31, 1],
                      [56, 'PharmacyType', '', 31, 1],
                      [57, 'HomeCareCentreType', '', 31, 1],
                      [58, 'MedicineType', '', 31, 1],
                      [59, 'EducationType', '', 31, 1],
                      [60, 'SpecializationType', '', 31, 1],
                      [61, 'CertificationType', '', 31, 1],
                      [62, 'UniversityMaster', '', 31, 1],
                      [63, 'CollegeMaster', '', 31, 1],
                      [64, 'ProfessionalTypeMaster', '', 31, 1],
                      [65, 'ProfessionalSubTypeMaster', '', 31, 1],
                      [66, 'SpecialityMaster', '', 31, 1],
                      [67, 'PathologyTestTypeMaster', '', 31, 1],
                      [68, 'TherapyTypeMaster', '', 31, 1],
                      [69, 'TherapyActivityTypeMaster', '', 31, 1],
                      [70, 'PathologyLabTestMaster', '', 31, 1],
                      [71, 'LabTestReportParametersMaster', '', 31, 1],
                      [72, 'ProcedureMaster', '', 31, 1],
                      [73, 'ProcedureDetailsMaster', '', 31, 1],
                      [74, 'TherapyMaster', '', 31, 1],
                      [75, 'TherapyActivityMaster', '', 31, 1],
                      [76, 'PaymentHeadsMaster', '', 31, 1],
                      [77, 'MedicineGroupMaster', '', 31, 1],
                      [78, 'PharmaceuticalCompanyMaster', '', 31, 1],
                      [79, 'MedicineStrengthMaster', '', 31, 1],
                      [80, 'MedicineUnitsMaster', '', 31, 1],
                      [81, 'MedicineMaster', '', 31, 1],
                      [82, 'MedicineRatesMaster', '', 31, 1],
                      [83, 'Onboarding', '', 83, 1],
                      [84, 'HealthProfessional', '', 83, 1],
                      [85, 'HealthProfessionalClinic', '', 83, 1],
                      [86, 'Franchise', '', 83, 1],
                      [87, 'Clinic', '', 83, 1],
                      [88, 'ThirdPartyVendor', '', 83, 1],
                      [89, 'Approval', '', 89, 1],
                      [90, 'HealthProfessional', '', 89, 1],
                      [91, 'Franchise', '', 89, 1],
                      [92, 'Clinic', '', 89, 1],
                      [93, 'ThirdPartyVendor', '', 89, 1],
                      [94, 'Groups&Roles', '', 94, 1],
                      [95, 'Add-Edit-MenuItem', '', 94, 1],
                      [96, 'Add-Edit-Role', '', 94, 1],
                      [97, 'Add-Edit-Group', '', 94, 1],
                      [98, 'UserMaster', '', 94, 1],
                      [99, 'RateCard', '', 99, 1],
                      [100, 'Add-Edit-DoctorConsultationCharges', '', 99, 1],
                      [101, 'Add-Edit-TherapistConsultationCharges', '', 99, 1],
                      [102, 'Add-Edit-PathologyCharges', '', 99, 1],
                      [103, 'Add-Edit-ProcedureCharges', '', 99, 1],
                      [104, 'Add-Edit-TherapyCharges', '', 99, 1],
                      [105, 'Add-Edit-MedicineRates', '', 99, 1],
                      [106, 'MasterScreens', '', 106, 1],
                      [107, 'AdminUser', '', 106, 1],
                      [108, 'DoctorWallet', '', 106, 1],
                      [109, 'PatientWallet', '', 106, 1]]

    for i in range(len(menu_item_list)):
        print(f'{i} : ', menu_item_list[i])
        MenuItemId = menu_item_list[i][0]
        MenuItemName = menu_item_list[i][1]
        MenuItemDesc = menu_item_list[i][2]
        MainMenuId = menu_item_list[i][3]
        ClinicId = menu_item_list[i][4]
        menu_items = MstMenuItem(
            MenuItemId=MenuItemId,
            MenuItemName=MenuItemName,
            MenuItemDesc=MenuItemDesc,
            MainMenuId=MainMenuId,
            WebpageLink='#',
            ClinicId=ClinicId,
            ActiveFlag='A',
            CreatedBy=1,
            UpdatedBy=1)
        try:
            menu_items.save()
        except:
            return None
