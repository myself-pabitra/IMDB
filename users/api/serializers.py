from django.contrib.auth.models import User
from rest_framework import serializers


class User_Register_Serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password','password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
              'style': {'input_type':'password'}
            }
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password!= password2:
            raise serializers.ValidationError({'Error':'Passwords do not match'})

        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error':'Email already exists'})


        account = User(email = self.validated_data['email'], username= self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account