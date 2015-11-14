from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Groups
    url('^groups/$', login_required(views.GroupListView.as_view()), name="group_list"),
    url('^groups/new/$', login_required(views.GroupCreateView.as_view()), name="group_create"),
    url('^groups/(?P<slug>[\w-]+)/update/$', login_required(views.GroupUpdateView.as_view()), name="group_update"),
    url('^groups/(?P<slug>[\w-]+)/delete/$', login_required(views.GroupDeleteView.as_view()), name="group_delete"),
    url('^groups/(?P<slug>[\w-]+)/$', login_required(views.GroupDetailView.as_view()), name="group_detail"),

    # Projects
    url('projects/$', views.ProjectListView.as_view(), name="project_list"),
    url('projects/create/$', login_required(views.ProjectCreateView.as_view()), name="project_create"),
    url('projects/(?P<slug>[\w-]+)/$', login_required(views.ProjectDetailView.as_view()), name="project_detail"),
    url('projects/(?P<slug>[\w-]+)/update/$', login_required(views.ProjectUpdateView.as_view()), name="project_update"),
    url('projects/(?P<slug>[\w-]+)/delete/$', login_required(views.ProjectDeleteView.as_view()), name="project_delete"),

    # Categories
    url('^categories/$', login_required(views.CategoryListView.as_view()), name="category_list"),
    url('^categories/new/$', login_required(views.CategoryCreateView.as_view()), name="category_create"),
    url('^categories/(?P<slug>[\w-]+)/update/$', login_required(views.CategoryUpdateView.as_view()), name="category_update"),
    url('^categories/(?P<slug>[\w-]+)/delete/$', login_required(views.CategoryDeleteView.as_view()), name="category_delete"),
    url('^categories/(?P<slug>[\w-]+)/$', login_required(views.CategoryDetailView.as_view()), name="category_detail"),

    # Rooms
    url('^rooms/$', login_required(views.RoomListView.as_view()), name="room_list"),
    url('^room/new/$', login_required(views.RoomCreateView.as_view()), name="room_create"),
    url('^room/(?P<slug>[\w-]+)/update/$', login_required(views.RoomUpdateView.as_view()), name="room_update"),
    url('^room/(?P<slug>[\w-]+)/delete/$', login_required(views.RoomDeleteView.as_view()), name="room_delete"),
    url('^room/(?P<slug>[\w-]+)/$', login_required(views.RoomDetailView.as_view()), name="room_detail"),

    # Items
    url('^items/$', login_required(views.ItemListView.as_view()), name="item_list"),
    url('^item/new/$', login_required(views.ItemCreateView.as_view()), name="item_create"),
    url('^item/(?P<pk>\d+)/update/$', login_required(views.ItemUpdateView.as_view()), name="item_update"),
    url('^item/(?P<pk>\d+)/delete/$', login_required(views.ItemDeleteView.as_view()), name="item_delete"),
    url('^item/(?P<pk>\d+)/$', login_required(views.ItemDetailView.as_view()), name="item_detail"),

    #AddOn
    url('^addons/$', login_required(views.AddOnListView.as_view()), name="addon_list"),
    url('^addon/new/$', login_required(views.AddOnCreateView.as_view()), name="addon_create"),
    url('^addon/(?P<pk>\d+)/update/$', login_required(views.AddOnUpdateView.as_view()), name="addon_update"),
    url('^addon/(?P<pk>\d+)/delete/$', login_required(views.AddOnDeleteView.as_view()), name="addon_delete"),
    url('^addon/(?P<pk>\d+)/$', login_required(views.AddOnDetailView.as_view()), name="addon_detail"),
    
    # Contacts
    url('^contacts/$', login_required(views.ContactListView.as_view()), name="contact_list"),
    url('^contact/new/$', login_required(views.ContactCreateView.as_view()), name="contact_create"),
    url('^contact/(?P<slug>[\w-]+)/update/$', login_required(views.ContactUpdateView.as_view()), name="contact_update"),
    url('^contact/(?P<slug>[\w-]+)/delete/$', login_required(views.ContactDeleteView.as_view()), name="contact_delete"),
    url('^contact/(?P<slug>[\w-]+)/$', login_required(views.ContactDetailView.as_view()), name="contact_detail"),
]
