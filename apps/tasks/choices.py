from django.db import models


class Status(models.TextChoices):
        TODO = "todo", "К выполнению"
        IN_PROGRESS = "in_progress", "В процессе"
        DONE = "done", "Выполнено"