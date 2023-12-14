<<<<<<< HEAD
# # from django.contrib.auth.models import User
# from django.db import models
#
#
=======
# from django.contrib.auth.models import User
# from django.db import models


>>>>>>> 8bd2625677363acd3021b60a4b29a30efde36d78
# class Menu(models.Model):
#     menu_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=50)
#     active = models.BooleanField(default=True)
#     create_date = models.DateField(auto_now_add=True)
#     update_date = models.DateField(auto_now=True)
<<<<<<< HEAD
#
#     # def __str__(self):
#     #     return self.name
#
#
=======

#     # def __str__(self):
#     #     return self.name


>>>>>>> 8bd2625677363acd3021b60a4b29a30efde36d78
# class SubMenu(models.Model):
#     sub_menu_id = models.AutoField(primary_key=True)
#     menu = models.ForeignKey(Menu, on_delete=models.RESTRICT)
#     name = models.CharField(max_length=50)
#     link = models.CharField(max_length=200)
#     desc = models.CharField(max_length=50)
#     active = models.BooleanField(default=True)
#     create_date = models.DateField(auto_now_add=True)
#     update_date = models.DateField(auto_now=True)
