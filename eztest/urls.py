"""eztest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from chat.views import index
from eztest.views import *
from django.contrib.auth.views import login



urlpatterns = [
    url(r'^$', login),
    url(r'^home/$', index, name="chat_index"),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^admin/', admin.site.urls),
    url(r'^api/chat/', include('chat.urls', namespace="chat_apis")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

