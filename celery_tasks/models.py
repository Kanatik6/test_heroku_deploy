from django.db import models


class testmodel(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=30)
    