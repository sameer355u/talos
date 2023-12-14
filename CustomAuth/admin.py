from django.contrib import admin
from CustomAuth.models import User, ProfessionalType
from CustomAuth.permissions import Permission, ProfessionPermission, UserProfession
from CustomAuth import models_grp_role

admin.site.register(User)
admin.site.register(ProfessionalType)
admin.site.register(Permission)
admin.site.register(ProfessionPermission)
admin.site.register(UserProfession)

admin.site.register(models_grp_role.MstGroup)
admin.site.register(models_grp_role.MstRole)
admin.site.register(models_grp_role.MstMenuItem)
admin.site.register(models_grp_role.MstGroupRole)
admin.site.register(models_grp_role.MstRoleMenuItem)
admin.site.register(models_grp_role.MstUserGroup)
