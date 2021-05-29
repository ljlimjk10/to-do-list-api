from django.db import models
from . import User

# Create your models here.
class Tasks(models.Model):
    created = models.DateTimeField(verbose_name='Date Created',auto_now_add=True)
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(null=False)
    status = models.CharField(max_length=100,blank=False,null=False)
    user = models.ForeignKey('User', related_name='tasks',null=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']
    
    