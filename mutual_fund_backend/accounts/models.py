from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']


class FundFamily(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Scheme(models.Model):
    fund_family = models.ForeignKey(FundFamily, on_delete=models.CASCADE, related_name="schemes")
    scheme_name = models.CharField(max_length=255)
    scheme_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.scheme_name
