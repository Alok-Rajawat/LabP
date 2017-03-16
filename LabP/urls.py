from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home_page.urls')),
    url(r'^login/', include('login_page.urls')),
    url(r'^register/', include('registration_page.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
]
