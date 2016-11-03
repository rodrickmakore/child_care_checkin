from django.contrib import admin
from app.models import Profile, ChildStatus

admin.site.register([Profile, ChildStatus])
