
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
import debug_toolbar

from core.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls"), name="blog-urls"),
    path("summernote/", include("django_summernote.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
