from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class CustomerProfile(models.Model):
    created_by = models.ForeignKey('auth.User', null=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    code = models.CharField(max_length=4)

    def last_report(self):
        return ChildReport.objects.filter(profile=self.id).last()

    @property
    def on_site(self):
        last_report = ChildReport.objects.filter(profile=self.id).last()
        if last_report.action == "i":
            return True
        return False

    def __str__(self):
        return self.parent_name

STATUS = [
    ("i", "Check-In"),
    ("o", "Check-Out")
]

class ChildReport(models.Model):
    profile = models.ForeignKey(CustomerProfile)
    action = models.CharField(max_length=1, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.child_name
