from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Userdaylog, Usergoals, Userinfo
from cs415.serializers import UserSerializer, UserdaylogSerializer, UsergoalsSerializer, UserinfoSerializer

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


