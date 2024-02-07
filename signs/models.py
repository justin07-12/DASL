from django.db import models


"""
A sign is an asl sign that has certain parameters that can be used to sort it.
We sort by charfields as not to limit ourselves at multiple instances.
"""
class Sign(models.Model):
    sign_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    handshape = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    palm_orientation = models.CharField(max_length=200)
    movement = models.BooleanField()

    #created_by = models.ForeignKey()

"""
Demonstrations are attached to signs. They can be images or videos.
"""
class Demonstration(models.Model):
    #user
    pub_date = models.DateTimeField("date published")
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)


class Set(models.Model):
    contained_signs = models.ManyToManyField("Sign", related_name = "signs")
