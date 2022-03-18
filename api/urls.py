from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('video/', include('videos.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
