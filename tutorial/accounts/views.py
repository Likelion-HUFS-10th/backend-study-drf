from django.shortcuts import render
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    print("STEP1")
    password = serializer.initial_data['password']
    print(password)
    print(CustomUser.objects.get(pk=6).password)
    print(make_password(password) == CustomUser.objects.get(pk=6).password)
    print(serializer.is_valid(raise_exception=True))
    if serializer.is_valid():
        print("STEP2")
        user = auth.authenticate(
            request=request,
            username=serializer.data['username'],
            password=serializer.data['password']
        )
        if user is not None:
            print("STEP3")
            auth.login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.save(password = make_password(serializer.validated_data['password']))
        auth.login(request, new_user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response(status=status.HTTP_200_OK)

