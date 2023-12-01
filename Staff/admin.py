from django.contrib import admin
# from CustomAuth.models import ProfessionalType
from Staff.models.doctor import TblDoctorSlot, TblDoctorSchedule
from Staff.models.clinic import Clinic, Lab, LabTest, LabReportParameter
from Staff.models.menu_items import Menu, SubMenu
from Staff.models.professional_Onboarding import HealthProfessionalPersonalDetails, HealthProfessionalEducationDetails, HealthProfessionalSpecializationDetails, HealthProfessionalExperienceDetails, HealthProfessionalBankDetails, HealthProfessionalCertificationDetails, HealthProfessionalDocumentLinks, MstUniversity, MstCollege, MstFlag


class AdminUser(admin.ModelAdmin):
    list_display = []


class AdminProfessionalType(admin.ModelAdmin):
    list_display = ['id', 'name']


# class AdminClinicProfessional(admin.ModelAdmin):
#     list_display = []


class AdminSlot(admin.ModelAdmin):
    list_display = []


class AdminDoctor(admin.ModelAdmin):
    list_display = []


class AdminClinic(admin.ModelAdmin):
    list_display = ['clinic_name', 'user', 'create_date', 'create_time', 'update_date', 'update_time']


class AdminLab(admin.ModelAdmin):
    list_display = []


class AdminLabTest(admin.ModelAdmin):
    list_display = []


class AdminLabReportParameter(admin.ModelAdmin):
    list_display = []


class AdminMenu(admin.ModelAdmin):
    list_display = []


class AdminSubMenu(admin.ModelAdmin):
    list_display = []


class AdminTblDoctorSchedule(admin.ModelAdmin):
    list_display = ['Day', 'StartDate', 'EndDate', 'SlotDuration', 'NoofSlots', 'StartTime']


class AdminTblDoctorSlot(admin.ModelAdmin):
    list_display = ['SlotDate', 'Day', 'StartTime', 'EndTime', 'Status']


# admin.site.register(ProfessionalType, AdminProfessionalType)
# admin.site.register(ClinicProfessional, AdminClinicProfessional)

admin.site.register(TblDoctorSchedule, AdminTblDoctorSchedule)
admin.site.register(TblDoctorSlot, AdminTblDoctorSlot)
admin.site.register(Clinic, AdminClinic)
admin.site.register(Lab, AdminLab)
admin.site.register(LabTest, AdminLabTest)
admin.site.register(LabReportParameter, AdminLabReportParameter)
admin.site.register(Menu, AdminMenu)
admin.site.register(HealthProfessionalPersonalDetails)
admin.site.register(HealthProfessionalEducationDetails)
admin.site.register(HealthProfessionalSpecializationDetails)
admin.site.register(HealthProfessionalExperienceDetails)
admin.site.register(HealthProfessionalCertificationDetails)
admin.site.register(HealthProfessionalDocumentLinks)
admin.site.register(HealthProfessionalBankDetails)
admin.site.register(MstUniversity)
admin.site.register(MstCollege)
admin.site.register(MstFlag)
admin.site.site_header = "eSwasthalya e-Clinic"
admin.site.site_title = "e-Clinic"
