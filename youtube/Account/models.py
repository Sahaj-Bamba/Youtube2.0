from django.db import models
from django.contrib.auth.models import User

class User_details(models.Model):

    GENDER_CHOICES =(
        ('F', 'Female'),
        ('M', 'Male')
    )

    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    authority = models.IntegerField(verbose_name="authority", default=0)
    type = models.IntegerField(verbose_name="type", default=0)
    user_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

