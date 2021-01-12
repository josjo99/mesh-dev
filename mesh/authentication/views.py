from django.shortcuts import render
from rest_framework import generics,permissions,views,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from knox.models import AuthToken

from .serializers import LoginSerializer, UserSerializer,RegistrationSerializer

# Create your views here.

class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user":UserSerializer(user,context=self.get_serializer_context()).data,
                "token":AuthToken.objects.create(user)[1],
            }
        )


@api_view(['POST'])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			#token = Token.objects.get(user=account).key
			#data['token'] = token
		else:
			data = serializer.errors
		return Response(data) 