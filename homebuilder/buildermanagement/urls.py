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
]
