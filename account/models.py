from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class UserManager(BaseUserManager):
    def create_user(self, email, password):
        "Creates and saves an User with given email and password"

        if not email:
            raise ValueError("User must have an valid email address.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_field.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        "Creates and saves an superuser with given email and password"
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_customer = True
        user.is_seller = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Django bydefault takes usename for login but here it wil take email
    USERNAME_FIELD = 'email'

    #Django create user by UserManager() now otherwise it creates by default.
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Only superuser have permission to access all data
        return self.is_superuser

    def has_module_perms(self, app_label):
        "Does the user have a permission to view the app `app_label`?"
        return self.is_superuser
