from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Groups
    url(r'^groups/$', login_required(views.GroupListView.as_view()), name="group_list"),
    url(r'^groups/new/$', login_required(views.GroupCreateView.as_view()), name="group_create"),
    url(r'^groups/(?P<slug>[\w-]+)/update/$', login_required(views.GroupUpdateView.as_view()), name="group_update"),
    url(r'^groups/(?P<slug>[\w-]+)/delete/$', login_required(views.GroupDeleteView.as_view()), name="group_delete"),
    url(r'^groups/(?P<slug>[\w-]+)/$', login_required(views.GroupDetailView.as_view()), name="group_detail"),

    # Projects
    url(r'projects/$', views.ProjectListView.as_view(), name="project_list"),
    url(r'projects/create/$', login_required(views.ProjectCreateView.as_view()), name="project_create"),
    url(r'projects/(?P<slug>[\w-]+)/$', login_required(views.ProjectDetailView.as_view()), name="project_detail"),
    url(r'projects/(?P<slug>[\w-]+)/update/$', login_required(views.ProjectUpdateView.as_view()), name="project_update"),
    url(r'projects/(?P<slug>[\w-]+)/delete/$', login_required(views.ProjectDeleteView.as_view()), name="project_delete"),

    # Categories
    url(r'^categories/$', login_required(views.CategoryListView.as_view()), name="category_list"),
    url(r'^categories/new/$', login_required(views.CategoryCreateView.as_view()), name="category_create"),
    url(r'^categories/(?P<slug>[\w-]+)/update/$', login_required(views.CategoryUpdateView.as_view()), name="category_update"),
    url(r'^categories/(?P<slug>[\w-]+)/delete/$', login_required(views.CategoryDeleteView.as_view()), name="category_delete"),
    url(r'^categories/(?P<slug>[\w-]+)/$', login_required(views.CategoryDetailView.as_view()), name="category_detail"),

    # Rooms
    url(r'^rooms/$', login_required(views.RoomListView.as_view()), name="room_list"),
    url(r'^room/new/$', login_required(views.RoomCreateView.as_view()), name="room_create"),
    url(r'^room/(?P<slug>[\w-]+)/update/$', login_required(views.RoomUpdateView.as_view()), name="room_update"),
    url(r'^room/(?P<slug>[\w-]+)/delete/$', login_required(views.RoomDeleteView.as_view()), name="room_delete"),
    url(r'^room/(?P<slug>[\w-]+)/$', login_required(views.RoomDetailView.as_view()), name="room_detail"),

    # Items
    url(r'^items/$', login_required(views.ItemListView.as_view()), name="item_list"),
    url(r'^item/new/$', login_required(views.ItemCreateView.as_view()), name="item_create"),
    url(r'^item/(?P<pk>\d+)/update/$', login_required(views.ItemUpdateView.as_view()), name="item_update"),
    url(r'^item/(?P<pk>\d+)/delete/$', login_required(views.ItemDeleteView.as_view()), name="item_delete"),
    url(r'^item/(?P<pk>\d+)/$', login_required(views.ItemDetailView.as_view()), name="item_detail"),

    #AddOn
    url(r'^addons/$', login_required(views.AddOnListView.as_view()), name="addon_list"),
    url(r'^addon/new/$', login_required(views.AddOnCreateView.as_view()), name="addon_create"),
    url(r'^addon/(?P<pk>\d+)/update/$', login_required(views.AddOnUpdateView.as_view()), name="addon_update"),
    url(r'^addon/(?P<pk>\d+)/delete/$', login_required(views.AddOnDeleteView.as_view()), name="addon_delete"),
    url(r'^addon/(?P<pk>\d+)/$', login_required(views.AddOnDetailView.as_view()), name="addon_detail"),
    
    # Contacts
    url(r'^contacts/$', login_required(views.ContactListView.as_view()), name="contact_list"),
    url(r'^contact/new/$', login_required(views.ContactCreateView.as_view()), name="contact_create"),
    url(r'^contact/(?P<slug>[\w-]+)/update/$', login_required(views.ContactUpdateView.as_view()), name="contact_update"),
    url(r'^contact/(?P<slug>[\w-]+)/delete/$', login_required(views.ContactDeleteView.as_view()), name="contact_delete"),
    url(r'^contact/(?P<slug>[\w-]+)/$', login_required(views.ContactDetailView.as_view()), name="contact_detail"),

    # Phases
    url(r'^phases/$', login_required(views.PhaseListView.as_view()), name="phase_list"),
    url(r'^phase/new/$', login_required(views.PhaseCreateView.as_view()), name="phase_create"),
    url(r'^phase/(?P<slug>[\w-]+)/update/$', login_required(views.PhaseUpdateView.as_view()), name="phase_update"),
    url(r'^phase/(?P<slug>[\w-]+)/delete/$', login_required(views.PhaseDeleteView.as_view()), name="phase_delete"),
    url(r'^phase/(?P<slug>[\w-]+)/$', login_required(views.PhaseDetailView.as_view()), name="phase_detail"),

    # Dashboard Pages
    url(r'^/$', login_required(views.HomePageView.as_view()), name="home"),
]
