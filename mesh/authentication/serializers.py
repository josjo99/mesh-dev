from rest_framework import serializers

from . import models

from django.contrib.auth import authenticate

models.CustomUser._meta.get_field('email')._unique = True

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email','password')

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")

class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = models.CustomUser
		fields = ['email', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):
		account = models.CustomUser(email=self.validated_data['email'],)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account