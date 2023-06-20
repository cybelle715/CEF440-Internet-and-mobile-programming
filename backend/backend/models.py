from django.db import models
from datetime import datetime
import uuid


class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uname = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30, blank= True)
    verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, default='Normal')
    picture = models.ImageField()
    town = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.uname



class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.TextField()
    quantity = models.IntegerField()
    poster = models.ForeignKey('Users', on_delete = models.CASCADE, related_name= 'post' )
    date_created = models.DateTimeField(auto_now_add=True)
    stop_date = models.DateTimeField()
    updatedAt = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey('Users', on_delete = models.CASCADE, related_name = 'send')
    receiver = models.ForeignKey('Users', on_delete = models.CASCADE, related_name = 'receive')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey('Food', on_delete = models.CASCADE, related_name='rate')
    user =  models.ForeignKey('Users', on_delete = models.CASCADE, related_name='rating')
    stars = models.PositiveIntegerField(default = 0)
    poster = models.ForeignKey('Users', on_delete = models.CASCADE, related_name='rated')
    
    def __str__(self):
        return self.user + "  " +self.content + "  -  " + self.poster

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food = models.ForeignKey('Food', on_delete = models.CASCADE, related_name='commented')
    user =  models.ForeignKey('Users', on_delete = models.CASCADE, related_name='commenting')
    content = models.TextField()
    poster = models.ForeignKey('Users', on_delete = models.CASCADE, related_name='posting')
    def __str__(self):
        return self.user + "  " +self.content + "  -  " + self.poster