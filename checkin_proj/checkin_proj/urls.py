from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexView, ProfileView, ProfileCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_profile/$', ProfileCreateView.as_view(), name="profile_create_view"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile_view"),

]
