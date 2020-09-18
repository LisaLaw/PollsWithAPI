from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('polls/', include('polls.urls', namespace="polls")),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]