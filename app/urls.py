from django.urls import path, include, reverse_lazy
from django.contrib.auth import urls as auth_urls
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('account/', include(auth_urls)),
    path('request', views.RequestFormView.as_view(), name='request-form'),
    path('req', views.RequestsView.as_view(), name='form'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('login/', LoginView.as_view(success_url=reverse_lazy('form')), name='login'),
]