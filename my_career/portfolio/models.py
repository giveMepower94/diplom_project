from django.db import models


class Client(models.Model):
    class Status(models.IntegerChoices):
        UNCHECKED = 0, 'Не просмотрено'
        CHECKED = 1, 'Просмотрено'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    resume = models.TextField(blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.UNCHECKED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

