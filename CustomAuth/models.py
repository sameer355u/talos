from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from django.db.models import Q


class ProfessionalType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    @staticmethod
    def get_profession_by_id(profession_id):
        return ProfessionalType.objects.get(id=profession_id)

    @staticmethod
    def get_patient_profession_obj():
        return ProfessionalType.objects.get(name='Patient')

    @staticmethod
    def get_professions():
        return ProfessionalType.objects.filter(~Q(name__in=['Patient', 'Admin']))

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, phone, password, email, profession):
        if not phone:
            raise ValueError('Mobile number is required.')
        user = self.model(phone=phone, email=email, profession=profession)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, email, profession):
        user = self.create_user(phone, password, email, profession)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    # username = None
    profession = models.ForeignKey(ProfessionalType, on_delete=models.RESTRICT)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=13, null=False, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'profession']
    objects = UserManager()

    @staticmethod
    def isExistsPhone(phone):
        if User.objects.filter(phone=phone).exists():
            return True
        else:
            return False

    def isExistsEmail(self):
        if User.objects.filter(email=self.email).exists():
            return True
        else:
            return False



    class Meta:

        permissions = (
            ("Doctor_dashboard", "Doctor_dashboard"),
            ("Patient_dashboard", "Patient_dashboard"),
            ("Others_dashboard", "Others_dashboard"),)

    def __str__(self):
        return self.email


class Profile(User):
    Address1 = models.CharField(max_length=50)
