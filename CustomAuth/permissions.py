from django.db import models
from CustomAuth.models import ProfessionalType
from rest_framework.permissions import BasePermission
from CustomAuth.models import User


class Permission(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ProfessionPermission(models.Model):
    professional_type = models.ForeignKey(ProfessionalType, on_delete=models.RESTRICT)
    permission = models.ManyToManyField(Permission)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


class UserProfession(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    professional_type = models.ForeignKey(ProfessionalType, on_delete=models.RESTRICT)
    permission = models.ManyToManyField(Permission, blank=True)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
