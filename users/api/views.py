from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import User_Register_Serializer


#Commenting models import to prevent auto generate token when a user loggedin or register cause we are using JWT authentication now.
from users import models

@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        serializer = User_Register_Serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration successful. Account has created successfully"
            data['username'] = account.username
            data['email'] = account.email

            # This below code works for Token Authentication
            token = Token.objects.get(user= account).key
            data['token'] = token


            # This below code works for Token Authentication
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
                

            # }

        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)




        
@api_view(['POST'])
def user_logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"success":"Logout successfully"}, status=status.HTTP_200_OK)
        