from django.conf import settings
from django.conf.urls import include, url, i18n, static

# ADMIN
from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n.i18n_patterns(
    '',

    # ADMIN
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # TinyMCE
    url(r'^tinymce/', include('tinymce.urls')),

    # CMS
    url(r'^', include('cms.urls')),

) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
