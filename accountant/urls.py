from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from stronghold.decorators import public


urlpatterns = patterns('',
    url(r'^', include('apps.pages.urls')),
    url(r'^', include('accounting.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^avatar/', include('avatar.urls')),
    url(r'^accounts/', include('allauth.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
