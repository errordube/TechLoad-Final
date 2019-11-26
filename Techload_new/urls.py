"""Techload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views as accounts_views  #new
from django.contrib.auth import views as auth_views #new
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),


     
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'),
    name='password_reset_form'), #new
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),
    name='password_reset_done'), #new
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'),
    name='password_reset_confirm'), #new
    path('password-reset-confirm/done',auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_compelete.html'),name='password_reset_complete'), #new
]
