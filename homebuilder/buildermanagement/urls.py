from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from . import views

urlpatterns = [
    url('groups/$', views.GroupListView.as_view(), name="group_list"),
]
