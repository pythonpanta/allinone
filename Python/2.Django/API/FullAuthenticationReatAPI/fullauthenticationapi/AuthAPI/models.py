from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/

class UserManager(BaseUserManager):
    def create_user(self, email, username,tc, password=None,password2=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            tc=tc   
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, tc,password=None):
        user = self.create_user(
          
            email=email,
            username=username,
            password=password,
            tc=tc,
         
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username= models.CharField(max_length=255)
    tc=models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
