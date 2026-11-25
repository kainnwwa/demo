from django.contrib import admin
from .models import MyUser, Service, Request

admin.site.register(MyUser)
admin.site.register(Service)
admin.site.register(Request)