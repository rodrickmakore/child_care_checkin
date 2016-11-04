from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    created_by = models.ForeignKey('auth.User', null=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)
    checked_in = models.BooleanField(default=False)

    def __str__(self):
        return self.parent_name

@receiver(post_save, sender='auth.user')
def create_profile(sender, **kwargs):
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        Profile.objects.create(user=instance)

STATUS = [
    ("i", "Check-In"),
    ("o", "Check-Out")
]
class ChildStatus(models.Model):
    profile = models.ForeignKey(Profile)
    status = models.CharField(max_length=1, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.child_name
