from django.db import models


class Reservation(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    message = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"
