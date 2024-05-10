from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=200, default = "")

    def __str__(self):
       return str(self.name)

class Sign(models.Model):
    sign_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    tags = models.ManyToManyField(Tag, null = True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    def __str__(self):
       return 'ASL: ' + str(self.sign_name)

class Demonstration(models.Model):
    pub_date = models.DateTimeField("date published")
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)

class Set(models.Model):
    contained_signs = models.ManyToManyField("Sign", related_name="signs")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
