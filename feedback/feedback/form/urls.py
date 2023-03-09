from django.urls import re_path as url

from . import views

app_name = 'form'
urlpatterns = [
    url(r'^$', views.feedback_form, name='home'),
]
