from django.db import models
from django.contrib.auth.models import User

class User_details(models.Model):

    GENDER_CHOICES =(
        ('F', 'Female'),
        ('M', 'Male')
    )

    user_reg_no = models.DecimalField(verbose_name="reg_no", max_digits=8, decimal_places=0, unique=True, blank=False)
    user_email = models.EmailField(verbose_name="email", max_length=100, unique=True, blank=False)
    user_name = models.CharField(verbose_name="name", max_length=100, blank=False)
    user_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user_cpi = models.DecimalField(verbose_name="cpi", max_digits=4, decimal_places=2, blank=False)
    user_contact = models.CharField(verbose_name="contact", blank=False, max_length=15)
    authority = models.IntegerField(verbose_name="authority", default=0)
    type = models.IntegerField(verbose_name="type", default=0)
    year = models.IntegerField(verbose_name="year", default=0)
    user_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)


    # user_email = models.CharField(verbose_name="email", max_length=100, default=1)
    # user_category = models.CharField(verbose_name="category", max_length=100, default=1)
    # user_password = models.CharField(verbose_name="password", max_length=100, default=1)
    # user_first_name = models.CharField(verbose_name="first_name", max_length=100, default=1)
    # user_last_name = models.CharField(verbose_name="last_name", max_length=100, default=1)
    # user_id = models.IntegerField(verbose_name="user_id", default=1)

    def __str__(self):
        return self.user_name

