from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Ares Taliwang'
admin.site.site_title = 'Ares Taliwang'
admin.site.index_title = 'Administrasi Situs'

urlpatterns = [
    path('admin/', admin.site.urls),
]
