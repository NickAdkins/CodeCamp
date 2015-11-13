from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from .views import GroupViewSet

urlpatterns = patterns('',
    url('', include(GroupViewSet().urls)),
)
