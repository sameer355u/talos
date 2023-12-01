from django.contrib import admin
from CustomAuth.models import User, ProfessionalType
from CustomAuth.permissions import Permission, ProfessionPermission, UserProfession


class AdminPermission(admin.ModelAdmin):
    list_display = ['code', 'name']


admin.site.register(User)
admin.site.register(ProfessionalType)
admin.site.register(Permission, AdminPermission)
admin.site.register(ProfessionPermission)
admin.site.register(UserProfession)
