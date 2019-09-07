from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class extendeduser(models.Model):
    phoneNumber = models.CharField(max_length = 15)
    dateOfBirth=models.DateField()
    gender=models.IntegerField(null=True)
    profileImage = models.ImageField(upload_to = 'media/', default = 'media/profileImage.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='getallall')


