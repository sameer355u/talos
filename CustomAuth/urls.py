from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from CustomAuth.views import user_registration, api_manager, views

urlpatterns = [

    path('api-register/', views.register_user, name='register'),
    path('api-login/', views.user_login, name='login'),
    path('api-logout/', views.user_logout, name='logout'),
    #  end api urls

    path("en/signup/", user_registration.multi_signup, name="account_signup"),
    path("signup/patient/", user_registration.signup_patient, name="signup_patient"),
    path("signup/staff/", user_registration.signup_staff, name="signup_staff"),

    path("check_login/<str:userid>/<str:password>/", api_manager.flutter_login, name="check_login"),

    path('userList/', api_manager.UserList.as_view({'get': 'list', 'post': 'create'}), name='userList'),
    path('userList/<int:pk>/', api_manager.UserList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userDetail'),

    path("profile/", TemplateView.as_view(template_name="dashboard.html"), name='profile'),
    path("user_profile/", TemplateView.as_view(template_name="account/profile.html"), name='user_profile'),
]
