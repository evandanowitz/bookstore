from django.db import models
from django.contrib.auth.models import User # needed for OneToOneField

# Create your models here.
class Salesperson(models.Model):
  username = models.OneToOneField (User, on_delete = models.CASCADE)
  bio = models.TextField(default = 'no bio...')
  name = models.CharField(max_length = 120)
  # 'customers' refers to a folder named 'customers' that'll be created by Django under the src/media folder
  pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

  def __str(self):
    return f'Profile of {self.user.username}'