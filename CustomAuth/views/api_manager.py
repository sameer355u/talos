from rest_framework import viewsets

from CustomAuth.serializers.serializers import UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from CustomAuth.models import User


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]


def flutter_login(request, userid, password):
    print("userid", userid)
    print("password", password)
    password = password
    get_user = User.objects.filter(email=userid, password=password)
    if get_user:
        return True
    else:
        return False
