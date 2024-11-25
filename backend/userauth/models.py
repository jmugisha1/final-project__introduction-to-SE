from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#
class customUserManager(BaseUserManager):
    def create_user(self, fullNames, email, password=None):

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model( fullNames=fullNames, email=email)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullNames, password=None):
        user = self.create_user(fullNames, email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


# Create your models here.
class customUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fullNames = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    objects = customUserManager()

    # for superUser creation
    REQUIRED_FIELDS = ['fullNames']
    USERNAME_FIELD = 'email'


    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"
    

    def __str__(self) -> str:
        return self.email
