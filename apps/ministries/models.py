from django.db import models
from apps.tasks.choices import Status

class Ministries(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(blank=False)
    # minister = models.ForeignKey(Minister)
    image = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Министерство'
        verbose_name_plural = 'Министерства'


class MinistryGoals(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=150,blank=False)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.TODO)
    ministry = models.ForeignKey(Ministries,on_delete=models.CASCADE,blank=False,related_name='goals')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Цели министерства'
        verbose_name_plural = 'Цели министерств'
        ordering = ['-created_at']

    def __str__(self):
        return self.name