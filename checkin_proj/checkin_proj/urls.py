from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexView, ProfileView, ProfileCreateView, StatusCreateView, ParentProfileView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_profile/$', ProfileCreateView.as_view(), name="profile_create_view"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile_view"),
    url(r'^create_status/$', StatusCreateView.as_view(), name="status_create_view"),
    url(r'^parent_view/(?P<pk>\d+)$', ParentProfileView.as_view(), name="parent_profile_view"),


]
