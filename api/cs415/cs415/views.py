from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Userdaylog, Usergoals, Userinfo
from cs415.serializers import UserSerializer, UserdaylogSerializer, UsergoalsSerializer, UserinfoSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication


class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class UserdaylogAPIView(APIView):
    def get(self,request):
        users = Userdaylog.objects.all()
        serializer = UserdaylogSerializer(users, many=True)
        return Response({'userdaylog': serializer.data})

class UsergoalsAPIView(APIView):
    def get(self,request):
        users = Usergoals.objects.all()
        serializer = UsergoalsSerializer(users, many=True)
        return Response({'usergoals': serializer.data})

class UserinfoAPIView(APIView):
    def get(self,request):
        users = Userinfo.objects.all()
        serializer = UserinfoSerializer(users, many=True)
        return Response({'usersinfo': serializer.data})

class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})

class GetSingleUserdaylogAPIView(APIView):
    def get(self,request,id):
        user = Userdaylog.objects.get(user_id=id)
        serializer = UserdaylogSerializer(user)
        return Response({'userinfo': serializer.data})

class GetSingleUsergoalAPIView(APIView):
    def get(self,request,id):
        user = Usergoals.objects.get(user_id=id)
        serializer = UsergoalsSerializer(user)
        return Response({'userinfo': serializer.data})

class GetSingleUserinfoAPIView(APIView):
    def get(self,request,id):
        user = Userinfo.objects.get(user_id=id)
        serializer = UserinfoSerializer(user)
        return Response({'userinfo': serializer.data})

