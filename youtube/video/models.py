from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class videoOrg(models.Model):
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    id2 = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class video(models.Model):
    id = models.AutoField(primary_key=True)
    org = models.ForeignKey(videoOrg, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    isPrivate = models.BooleanField(default=False)
    report = models.IntegerField(default=0)
    tags = models.ManyToManyField('tag')

    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=500, default="")


class tag(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name


#
# class playlist(models.Model):
#     name = models.CharField(max_length=500)
#     video = models.ManyToManyField('video')
#     owner = models.ForeignKey(User,on_delete=models.CASCADE())
#
#
# class PrimaryComment(models.Model):
#     content = models.CharField(max_length="500")
#     video = models.ManyToOneRel('video')
#     likeCount = models.IntegerField(max_length=10,default=0)
#
#
# class SecondaryComment(models.Model):
#     content = models.CharField(max_length="500")
#     comment = models.ManyToOneRel('SecondaryComment')
#     likeCount = models.IntegerField(max_length=10,default=0)
