from django.db import models


class EventBase(models.Model):
    date = models.DateField(blank=True,null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Events(EventBase):
    image = models.ImageField(upload_to='images',blank=False,null=True)


    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-created_at']

    
class EventPhoto(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"Фотография {self.event.name}"
    

class EventVideo(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos')


    def __str__(self):
        return f"Видео {self.event}"


class EventsToOrganize(EventBase):
    image = models.ImageField(upload_to='images',blank=True,null=True)
    


    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Мероприятие для организации"
        verbose_name_plural = "Мероприятия для организации"
        ordering = ['-created_at']


class YearPlan(models.Model):
    name = models.CharField(max_length=30,blank=False)
    description = models.TextField(blank=False)
    date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'План года'
        verbose_name_plural = 'План года'

    def __str__(self):
        return self.name


