from django.contrib import admin
from django.urls import path, include # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
