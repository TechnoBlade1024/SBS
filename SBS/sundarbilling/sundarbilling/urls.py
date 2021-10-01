"""sundarbilling URL Configuration"""
from django.contrib import admin
from django.urls import path, include
import sundarbilling.login
urlpatterns = [
    path('admin/', admin.site.urls)
]
