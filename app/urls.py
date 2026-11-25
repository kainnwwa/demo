from django.urls import path, include 
from django.contrib.auth import urls as auth_urls
from django.contrib.auth.views import LoginView




urlpatterns = [
    path('account/', include(auth_urls))
    path('my-login/'), LoginView.as_view(success_url=reverse('main')),
    name = 'login' ]
