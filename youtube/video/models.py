from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField('tag')



class tag(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
