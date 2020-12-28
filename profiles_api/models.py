from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class MyCustomUserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have a valid Username')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff     = True
        user.save(using=self._db)

        return user


class MyCustomUserProfile(AbstractBaseUser, PermissionsMixin):
    """DB model for users in the system"""
    email           = models.EmailField(max_length=50, unique=True)
    name            = models.CharField(max_length=50)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects         = MyCustomUserProfileManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of the user"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return self.email
