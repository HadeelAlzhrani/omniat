from django.db import models
from django.contrib.auth.models import User
import datetime # new

# Create your models here.
gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    )
class Profile (models.Model):
    """user_name=models.CharField(max_length=20)
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField (null=True)
    registration_date= models.DateTimeField(auto_now_add=True)"""

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth= models.DateField(blank=True, null=True)

    gender = models.CharField(
        max_length=1,
        choices=gender_choices,
    )
    avatar_image=models.ImageField (upload_to="images/", null=True)
    def __str__(self):
        return self.user.username


class Wish (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text= models.CharField(max_length= 140)
    published_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Comment (models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    wish= models.ForeignKey(Wish, on_delete=models.CASCADE)
    comment_text= models.CharField(max_length=140)
    comment_date= models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.comment_text

