from django.db import models
from django.contrib.auth.models import User

class User_details(models.Model):

    GENDER_CHOICES =(
        ('F', 'Female'),
        ('M', 'Male')
    )

    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.CharField(verbose_name="discription", max_length=100, blank=True)
    user_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    user_subscriber = models.ManyToManyField(User,related_name="subscriber")

    def __str__(self):
        return self.user_name


class Notification(models.Model):

    STATUS =(
        ('T', 'Pending'),
        ('F', 'Sent')
    )
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    content = models.CharField(verbose_name="discription", max_length=100, blank=True)
    status = models.CharField(max_length=1, choices=STATUS)
