from django.conf.urls import include, url,patterns
import os
from django.views.generic import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^', include('osiris.urls')),
    # # url(r'^blog/', include('blog.urls')),
    # url(r'^youtube/', include('django_youtube.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2callback', 'osiris.views.auth_return', name="oauth"),
]
