from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.category} - {self.amount}"
