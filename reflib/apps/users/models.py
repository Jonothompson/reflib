from django.db import models
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    # avatar_picture = models.ImageField(upload_to='profile_photos', null=True, blank=True)
