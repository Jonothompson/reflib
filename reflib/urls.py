from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^adpip min/', admin.site.urls),
    url(r'^', include('library.urls')),
    url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
]
