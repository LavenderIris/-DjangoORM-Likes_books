from __future__ import unicode_literals

from django.db import models

# Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Book(models.Model):
    name = models.CharField(max_length=255, null=True)
    desc = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(User, related_name = 'books', null=True)
    

class likes(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True)