from django.db import models
from django.contrib.auth import models as auth_models


class Namespace(models.Model):
    name = models.SlugField(primary_key=True)



class UserManager(auth_models.BaseUserManager):
    def create_user(self, name, password, is_superuser=False):
        u = User.objects.create(name=name, is_superuser=is_superuser)
        u.set_password(password)
        u.save()
        return u

    def create_superuser(self, name, password):
        return self.create_user(name, password, True)


class User(Namespace, auth_models.AbstractBaseUser):
    USERNAME_FIELD = 'name'
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
