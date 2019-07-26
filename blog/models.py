from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Tag(models.Model):

    title = models.CharField(max_length=150) 

    def __str__(self):

        return self.title        



class Tujruba(models.Model):

    photo = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=150) 
    description = models.TextField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title


class Comment(models.Model):
    tujruba = models.ForeignKey('Tujruba', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()

    def __str__(self):

        return self.author.username + ' on ' + self.tujruba.title



class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images')
    name = models.CharField(max_length=150)
    bio = models.TextField(default='', blank=True)
    job = models.CharField(max_length=150, default='', blank=True)
    age = models.CharField(max_length=150, default='', blank=True)
    country = models.CharField(max_length=150, default='', blank=True)
    facebook = models.URLField(max_length=200, default='', blank=True)
    instagram = models.URLField(max_length=200, default='', blank=True)
    twitter = models.URLField(max_length=200, default='', blank=True)
    personal_website = models.URLField(max_length=200, default='', blank=True)
    #followed_tag_ids
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username

    def save(self, *args, **kwargs):

        self.name = self.user.first_name + ' ' + self.user.last_name
        super().save(*args, **kwargs)

def create_profile(sender, **kwarg):

    if kwarg['created']:
        user_profile = Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)




class Star(models.Model):
    tujruba = models.ForeignKey('Tujruba', on_delete=models.CASCADE)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
