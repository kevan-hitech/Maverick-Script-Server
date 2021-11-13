from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registrator.urls')),
    path('', include('accounts.urls')),
    path('', include('addmac.urls')),
    path('', include('addssid.urls')),
    path('', include('scriptlog.urls')),
    path('', include('removemac.urls')),
    path('', include('removessid.urls')),
]

admin.site.site_header = "Javits Maverick Admin"
admin.site.site_title = "Javits Maverick"
admin.site.index_title = "Admin Page"
