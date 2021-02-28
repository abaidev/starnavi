from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None):
        if not email or not password:
            raise ValueError("Email and Password must be provided")
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, first_name=None):
        admin = self.create_user(email, password=password, first_name=first_name)
        admin.is_admin = True
        admin.save()
        return admin


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)   # can login
    is_admin = models.BooleanField(default=False)   # superuser
                                                    # TODO: make 'favorites' field (ManyToMany for Post)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    objects = UserManager()

    def __str__(self):
        return self.email


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=80)
    content = models.TextField(null=True, blank=True)
    image_cover = models.ImageField(null=True, blank=True, upload_to='posts/cover')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0) # TODO: make it ManyToMany for User

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # TODO: move this method to views
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)