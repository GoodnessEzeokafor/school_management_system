from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = False
        user_obj.admin = False
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj
    

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password
        )
        user.staff = True
        return user
    
    def create_superuser(self, email,password=None):
        user = self.create_user(
            email,
            password = password
        )
        user.active = True
        user.admin =True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add =True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    

    
    def has_perms(self, perm_list, obj=None):
        """
        Return True if the user has each of the specified permissions. If
        object is passed, check if the user has all required perms for it.
        """
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        return True 


    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.admin

    @property
    def is_admin(self):
        return self.admin
