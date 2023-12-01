from django.views.generic import RedirectView
from CustomAuth.forms import ProfessionalsSignupForm, PatientSignupForm
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from CustomAuth.models import User, ProfessionalType
from django.urls import reverse
from allauth.account.views import SignupView, LoginView

# class ProfessionalsSignupView(SignupView):
#     template_name = 'account/signup.html'
#     form_class = ProfessionalsSignupForm
#
#     def get_success_url(self):
#         return reverse("account_email_verification_sent")
#
#
# class PatientSignupView(SignupView):
#     template_name = 'account/signup.html'
#     form_class = PatientSignupForm
#
#     def get_success_url(self):
#         print("Entered.........")
#         return reverse("account_email_verification_sent")
# accounts/views.py

from rest_framework import status, permissions
from rest_framework.response import Response
from CustomAuth.serializers.serializers import UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from CustomAuth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# @api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            #print("Token: ", token)
            return Response({'status': "Success", "statusCode": status.HTTP_200_OK}, status=status.HTTP_200_OK)

        return Response(
            {'status': "Failure", "errorMessage": "Invalid credentials", "errorDescription": "Invalid credentials",
             "statusCode": status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
