from .models import User
from rest_framework import serializers 
from django.contrib.auth.hashers import make_password, check_password
from secrets import token_hex
import datetime

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'name','profile','budget','email','token','token_expires')

class UserUpdateSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(required=False)
    
    def validate(self, data):
        errors = {}
        if 'name' not in data or not data['name']:
             errors['name'] = ['name is required']
        if 'email' not in data or not data['email']:
            errors['email'] = ['email is required']
        if bool(errors):
            raise serializers.ValidationError(errors)
        
        return data
    class Meta:
        model = User
        fields = ('id', 'budget')

class UserSignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True  , required=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)
    profile = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('id','name','profile','email','password','token', 'token_expires')

    def create(self, validate_data):

        if User.objects.filter(email=validate_data['email']).exists():
             raise serializers.ValidationError({'email':['Email Alrady Exists']})
        validate_data["password"]=make_password(validate_data["password"])
        validate_data["token"]=token_hex(30)
        validate_data["token_expires"]=datetime.datetime.now()+datetime.timedelta(days=7)
        return super().create(validate_data)

class UserSignInSerializer(serializers.ModelSerializer):    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)
    profile = serializers.ImageField(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'profile', 'email', 'password', 'token', 'token_expires')
    
    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if len(user) > 0 and check_password(validated_data['password'], user[0].password):
            user[0].token = token_hex(30)
            user[0].token_expires = datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save()
            return user[0]
        else:
            raise serializers.ValidationError({"error": "The password or email is incorrect."})    

        

