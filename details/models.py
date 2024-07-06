from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length = 20)
    email = models.EmailField()
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Level(models.Model):
    level_number = models.SmallIntegerField()
    level_id = models.SmallIntegerField()
    level_description = models.TextField()

class Video(models.Model):
    video_name = models.CharField(max_length = 20)
    video_description = models.TextField()
    video_id = models.SmallIntegerField()
    level_id = models.SmallIntegerField()