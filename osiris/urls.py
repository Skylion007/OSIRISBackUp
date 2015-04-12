from django.conf.urls import include, url
from django.contrib import admin
import views
urlpatterns = [
    # Examples:
    # url(r'^$', include(osiris.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/',views.index, name= 'index'),
    url(r'^uploadsubmit/',views.upload, name= 'uploadsubmit'),
    url(r'^downloadsubmit/',views.download, name= 'downloadsubmit'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/', views.login, name = 'redirect'),
]
