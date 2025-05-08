from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    web = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
