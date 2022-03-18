from django.urls import path, include
from dj_rest_auth.urls import settings

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('video/', include('videos.urls')),
]
