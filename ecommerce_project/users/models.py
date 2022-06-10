from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    '''This is the UserManager class.

    It is the manager class of the User model that contains methods to deal with the User model.
    '''

    def _create_user(self, email, password, is_staff,
                     is_superuser, date_of_birth, gender, address,
                     user_type, name, is_active=True, shopname=None):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            user_type=user_type,
            name=name,
            shopname=shopname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, date_of_birth,
                    gender, address, user_type, name,
                    is_active=True, shopname=None):
        '''This is the create_user function.

        It internally calls the create_user method of UserManager 
        and creates a new user in the database.
        '''
        return self._create_user(email, password, False, False,
                                 date_of_birth, gender, address,
                                 user_type, name, is_active, shopname)

    def create_superuser(self, email, password, date_of_birth, gender, address, user_type, name):
        '''This is the create_superuser function.

        It calls the create_user method to create a super user/admin in the database.
        '''
        user = self._create_user(
            email, password, True, True, date_of_birth, gender, address, user_type, name)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''This is the User class.

    It is the model class for our User in the database.
    '''
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    USER_TYPES = (
        ('ADMIN', 'Admin'),
        ('SHOPUSER', 'Shopuser'),
        ('CUSTOMER', 'Customer'),
    )

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=254)
    user_type = models.CharField(max_length=8, choices=USER_TYPES)
    shopname = models.CharField(max_length=254, null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth',
                       'gender', 'address', 'user_type']

    objects = UserManager()
