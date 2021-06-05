from django.db import models
import os

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username}: {self.email}"

class Pictures(models.Model):
    uploaded_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=os.path.join(os.getcwd(), 'WebApp', 'Images'))

    def __str__(self):
        return f"{self.picture.path} by: {self.uploaded_by}"

class Friends(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(Users, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(Users, related_name="friend_set", on_delete=models.CASCADE)