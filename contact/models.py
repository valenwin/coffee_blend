from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField(null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name}, email: {self.email}"
