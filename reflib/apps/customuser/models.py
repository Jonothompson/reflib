from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    full_name = models.CharField('full name', max_length=255, blank=True)
    preferred_name = models.CharField('preferred name',
                                      max_length=255, blank=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.preferred_name
