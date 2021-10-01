"""sundarbilling URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include


from .views import login as sundarlogin
from .views import loginuser
from .views import reguser
app_name='login'
urlpatterns = [
    path('', sundarlogin,name='loginpage'),
    path('loginuser', loginuser,name='loginuser'),
    path('registeruser', reguser,name='reguser')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


