from django.contrib import admin
from django.urls import path,include


admin.site.site_header = 'Ludis Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('playground.urls')), 
    path('__debug__/', include('debug_toolbar.urls', namespace='djdt')),
    
]
