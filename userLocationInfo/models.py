from django.db import models


# Create your models here.

class UserInfo(models.Model):
    visitor_name = models.CharField(max_length=50)

    def __str__(self):
        return self.visitor_name
