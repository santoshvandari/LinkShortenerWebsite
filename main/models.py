from django.db import models

# Create your models here.
class URLTable(models.Model):
    url=models.CharField(max_length=1000)
    short_url=models.CharField(max_length=50,unique=True,blank=True,null=True)