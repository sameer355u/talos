from django.db import models
from django.db.models import Q
from CustomAuth.models import ProfessionalType, User


class MstGroup(models.Model):
    # Define the fields for the MstGroup model
    GroupId = models.AutoField(primary_key=True)
    GroupName = models.CharField(max_length=255)
    GroupDesc = models.CharField(max_length=255)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1)
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    @staticmethod
    def get_group_id_by_id(GroupId):
        return MstGroup.objects.get(GroupId=GroupId)

    @staticmethod
    def get_group_id_by_profession(request):
        return MstGroup.objects.get(GroupName=request.user.profession.name)


class MstRole(models.Model):
    # Define the fields for the MstRole model
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=255)
    RoleDesc = models.CharField(max_length=255)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1)
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    @staticmethod
    def get_role_id_by_id(RoleId):
        return MstRole.objects.get(RoleId=RoleId)


class MstMenuItem(models.Model):
    # Define the fields for the MstMenuItem model
    MenuItemId = models.AutoField(primary_key=True)
    MenuItemName = models.CharField(max_length=255)
    MenuItemDesc = models.CharField(max_length=255)
    MainMenuId = models.IntegerField()
    WebpageLink = models.CharField(max_length=255)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1)
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.MenuItemName

class MstGroupRole(models.Model):
    # Define the fields for the MstGroupRole model
    GrouproleId = models.AutoField(primary_key=True)
    GroupIdFK = models.ForeignKey(MstGroup, on_delete=models.CASCADE)
    RoleIdFK = models.ForeignKey(MstRole, on_delete=models.CASCADE)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1)
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    @staticmethod
    def get_grp_rol_by_grp_id(GroupIdFK):
        return MstGroupRole.objects.filter(GroupIdFK=GroupIdFK)

    @staticmethod
    def get_gro_role_by_profession(request):
        return MstGroupRole.objects.filter(GroupIdFK=MstGroup.get_group_id_by_profession(request))

class MstRoleMenuItem(models.Model):
    # Define the fields for the MstRoleMenuItem model
    RoleMenuItemId = models.AutoField(primary_key=True)
    RoleIdFK = models.ForeignKey(MstRole, on_delete=models.CASCADE)
    MenuItemIdFK = models.ForeignKey(MstMenuItem, on_delete=models.CASCADE)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1,default='A')
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    @staticmethod
    def get_role_menu_by_group_role_id(RoleIdFK):
        return MstRoleMenuItem.objects.filter(RoleIdFK=RoleIdFK)


class MstUserGroup(models.Model):
    UsergroupId = models.AutoField(primary_key=True)
    UserIdFK = models.ForeignKey(User,on_delete=models.CASCADE)
    GroupIdFK = models.ForeignKey(MstGroup,on_delete=models.CASCADE)
    ClinicId = models.IntegerField()
    ActiveFlag = models.CharField(max_length=1,default='A')
    CreatedBy = models.IntegerField()
    UpdatedBy = models.IntegerField()
    CreationDateTime = models.DateTimeField(auto_now_add=True)
    UpdationDateTime = models.DateTimeField(auto_now=True)
    DeleteFlag = models.CharField(max_length=1, default='A')

    @staticmethod
    def get_user_group_by_user_id(request):
        return MstUserGroup.objects.get(UserIdFK=request.user)
