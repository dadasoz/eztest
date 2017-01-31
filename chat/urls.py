from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^get-users/$', views.UsersList.as_view()),
    url(r'^get-messages/$', views.MessagesList.as_view()),
]