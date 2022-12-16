from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('', include('services.drf_yasg')),
   path('admin/', admin.site.urls),
   path('account/', include('apps.account.urls')),
   path('comments/', include('apps.comments.urls')),
   path('library/', include('apps.books.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)