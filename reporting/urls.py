from django.conf.urls import url
from . import views

app_name = "reporting"
urlpatterns = [
    url(r'', views.index, name='index'),
]

