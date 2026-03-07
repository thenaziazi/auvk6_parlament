from django.db import models
from apps.events.models import EventsToOrganize
from apps.ministries.models import Ministries
from apps.users.models import CustomUser


class Tasks(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "К выполнению"
        IN_PROGRESS = "in_progress", "В процессе"
        DONE = "done", "Выполнено"

    name = models.TextField(max_length=150, blank=False)
    description = models.TextField(max_length=250, blank=False)
    assigned_to = models.ForeignKey(CustomUser, models.DO_NOTHING)
    ministry = models.ForeignKey(
        Ministries,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    deadline = models.DateField()
    event = models.ForeignKey(
        EventsToOrganize,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Поручение"
        verbose_name_plural = "Поручения"

        
