from __future__ import unicode_literals

from django.db import models


# class LibraryPictures(models.Model):
#     title = models.CharField(max_length=100, blank=False, Null=False)
#     uploadedPicture = models.FileField(upload_to='')
#     tags = models.ManyToManyField(Tag)
#
#
# class Tag(models.Model):
#     word = models.CharField(max_length=35)
#     slug = models.CharField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=False)
#
#     def __unicode__(self):
#         return self.word
