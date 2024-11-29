from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    name = models.CharField(max_length=100)


    @property
    def amountOfUsers(self):
        return self.usersdeusers.count()
    
    @property
    def posts(self):
        return self.postsdeposts
    
    def __str__(self):
        return self.name


class UserC(AbstractUser):
    school = models.ForeignKey(School, related_name='usersdeusers', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'PersonalizedUser'
        verbose_name_plural = 'PersonalizedUsers'


    @property
    def posts(self):
        return self.usersdeposts
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(UserC, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    school = models.ForeignKey(School, related_name='postsdeposts', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(UserC, related_name='usersdeposts', on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



