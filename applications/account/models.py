from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

from blog_zi_ka.settings import EMAIL_HOST_USER


class UserManager(BaseUserManager):

    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        # user.is_active = True
        user.save() #using=self._db
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        # email = self.normalize_email(email)
        # user = self.model(email=email)
        # user.set_password(password)
        # user.is_active = True
        # user.is_staff = True
        # user.is_superuser = True
        # user.save(using=self._db)
        return self._create_user(email, password, **extra_fields)


class ContactMethod(models.TextChoices):
    whatsapp = ('whatsapp', 'WhatsApp')
    telephon = ('telephone', 'Phone number')
    mail = ('mail', 'Mail')


class User(AbstractUser):
    # username = None
    email = models.EmailField(primary_key=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    contact_number = models.CharField(max_length=50, blank=True)
    contact_method = models.CharField(max_length=50, blank=True, choices=ContactMethod.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(6, '0123456789')
        self.activation_code = code
        self.save()

    def activate_with_code(self, activation_code):
        if self.activation_code != activation_code:
            raise Exception('activation code is wrong')
        self.is_active = True
        self.activation_code = ''
        self.save()

    def send_activation_email(self):
        message = f'''thank you for registration your activation code is : http://localhost:8000/auth/account/activate/{self.activation_code}/'''

        send_mail('account activation ', message, EMAIL_HOST_USER, [send_mail],)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        