from django.db import models

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
