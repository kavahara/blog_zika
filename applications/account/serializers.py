from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.core.mail import send_mail

from blog_zi_ka.settings import EMAIL_HOST_USER

User = get_user_model()

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)
    password_confirmation = serializers.CharField(min_length=8, required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError ('this login is already registered')
        return email

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise serializers.ValidationError('ur password not match')
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.create_activation_code()
        user.send_activation_email()
        return user

class ChangePassword(serializers.Serializer):
    old_password = serializers.CharField(min_length=8, required=True)
    new_password = serializers.CharField(min_length=8, required=True)
    new_password_confirmation = serializers.CharField(min_length=8, required=True)

    def validate_old_password(self, old_pass):
        requests = self.context.get('request')
        user = requests.user
        if not user.check_password(old_pass):
            raise serializers.ValidationError('password didnt match')
        return old_pass

    def validate(self, attrs):
        new_pass1 = attrs.get('new_password')
        new_pass2 = attrs.get('new_password_confirmation')
        if new_pass1 != new_pass2:
            raise serializers.ValidationError('password didnt match')
        return attrs

    def set_new_password(self):
        new_pass = self.validated_data.get('new_password')
        user = self.context.get('request').user
        user.set_password(new_pass)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validated_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError ('user not found')
        return email

    def send_ver_email(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_mail(
            'Password recovery',
            f"""Your activation code is : http://localhost:8000/auth/account/forgot_password_complete/{user.activation_code}/""",
            EMAIL_HOST_USER,
            [user.email, ]
        )

class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)
    password_confirmation = serializers.CharField(min_length=8, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password1 = attrs.get('password')
        password2 = attrs.get('password_confirmation')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        if password1 != password2:
            raise serializers.ValidationError('password didnt match')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validated_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('bad credentials')
        return email

    def validated(self, data):
        requests = self.context.get('requests')
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(username=email, password=password, requests=requests)
            if not user:
                raise serializers.ValidationError('wrong email or password')
        else:
            raise serializers.ValidationError('email and password are required')
        data['user'] = user
        return data


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    last_name = serializers.CharField()
    contact_number = serializers.CharField()
    contact_method = serializers.CharField()

    class Meta:
        model = User
        fields = ('name', 'last_name', 'contact_number', 'contact_method')    #___all__

    def validate(self, data):
        name = data.get('name')
        lastname = data.get('lastname')
        contact_number = data.get('contact_number')
        contact_method = data.get('contact_method')

        return data
