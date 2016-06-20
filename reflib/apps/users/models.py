from authtools.models import AbstractEmailUser
from django.db import models


class User(AbstractEmailUser):
    related_name = models.CharField(max_length=25, blank=False, null=False)
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    # avatar_picture = models.ImageField(upload_to='profile_photos', null=True, blank=True)
