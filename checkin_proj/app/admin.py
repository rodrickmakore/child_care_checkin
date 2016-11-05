from django.contrib import admin
from app.models import CustomerProfile, ChildReport

admin.site.register([CustomerProfile, ChildReport])
