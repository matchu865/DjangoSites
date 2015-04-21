from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'projsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^golfers/', include('golfers.urls', namespace ="golfers")),
    url(r'^$', include('golfers.urls', namespace="golfers")),
]
