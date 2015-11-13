from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url('^groups/$', login_required(views.GroupListView.as_view()), name="group_list"),
    url('^groups/new/$', login_required(views.GroupCreateView.as_view()), name="group_create"),
    url('^groups/(?P<slug>[\w-]+)/update/$', login_required(views.GroupUpdateView.as_view()), name="group_update"),
    url('^groups/(?P<slug>[\w-]+)/delete/$', login_required(views.GroupDeleteView.as_view()), name="group_delete"),
    url('^groups/(?P<slug>[\w-]+)/$', login_required(views.GroupDetailView.as_view()), name="group_detail"),
    url('^categories/$', login_required(views.CategoryListView.as_view()), name="category_list"),
    url('^categories/new/$', login_required(views.CategoryCreateView.as_view()), name="category_create"),
    url('^categories/(?P<slug>[\w-]+)/update/$', login_required(views.CategoryUpdateView.as_view()), name="category_update"),
    url('^categories/(?P<slug>[\w-]+)/delete/$', login_required(views.CategoryDeleteView.as_view()), name="category_delete"),
    url('^categories/(?P<slug>[\w-]+)/$', login_required(views.CategoryDetailView.as_view()), name="category_detail"),
]
