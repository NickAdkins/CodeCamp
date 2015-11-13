from django.conf.urls import patterns, url, include
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from . import views

urlpatterns = [
    url('groups/$', views.GroupListView.as_view(), name="group_list"),

    url('contacts/$', views.ContactListView.as_view(), name="contact_list"),
    url('contacts/(?P<pk>\d+)/$', login_required(views.ContactDetailView.as_view()), name="contact_detail"),
    url('contacts/create/$', login_required(views.ContactCreateView.as_view()), name="contact_create"),
    url('contacts/(?P<pk>\d+)/update/$', login_required(views.ContactUpdateView.as_view()), name="contact_update"),
    url('contacts/(?P<pk>\d+)/delete/$', login_required(views.ContactDeleteView.as_view()), name="contact_delete"),

    url('projects/$', views.ProjectListView.as_view(), name="project_list"),
    url('projects/(?P<pk>\d+)/$', login_required(views.ProjectDetailView.as_view()), name="project_detail"),
    url('projects/create/$', login_required(views.ProjectCreateView.as_view()), name="project_create"),
    url('projects/(?P<pk>\d+)/update/$', login_required(views.ProjectUpdateView.as_view()), name="project_update"),
    url('projects/(?P<pk>\d+)/delete/$', login_required(views.ProjectDeleteView.as_view()), name="project_delete"),

    url('Items/$', views.ItemListView.as_view(), name="item_list"),
    url('Items/(?P<pk>\d+)/$', login_required(views.ItemDetailView.as_view()), name="item_detail"),
    url('Items/create/$', login_required(views.ItemCreateView.as_view()), name="item_create"),
    url('Items/(?P<pk>\d+)/update/$', login_required(views.ItemUpdateView.as_view()), name="item_update"),
    url('Items/(?P<pk>\d+)/delete/$', login_required(views.ItemDeleteView.as_view()), name="item_delete"),

]
