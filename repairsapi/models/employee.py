from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=155)

    @property
    def full_name(self):
        """Combines the first and last name property of employee to display on client side"""
        return f'{self.user.first_name} {self.user.last_name}'
