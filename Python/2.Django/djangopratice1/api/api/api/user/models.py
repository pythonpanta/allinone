from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
import uuid


def uuid_generate():
    return uuid.uuid4().hex



class Role(models.Model):
    id = models.CharField(
        max_length=32, default=uuid_generate, unique=True, primary_key=True)
    role = models.CharField(max_length=100)

    class Meta:
        db_table = 'role'


class User(AbstractUser, PermissionsMixin):
    id = models.CharField(max_length=32, primary_key=True,
                          unique=True, default=uuid_generate)
    email = models.EmailField(('email address'), unique=True)
    address = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(default=False)
    location = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    created_by = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name="+", db_column="created_by", null=True)
    citizenship_front_side = models.BinaryField(null=True)
    citizenship_back_side = models.BinaryField(null=True)
    pan_number = models.CharField(max_length=9, null=True)
    role = models.ForeignKey(
        Role, on_delete=models.PROTECT, related_name="+", null=True)
    category = models.ManyToManyField(
        "clg_api.Category", db_column='category_id', related_name="+", blank=True)
    otp = models.CharField(max_length=6, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'username']

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.id
