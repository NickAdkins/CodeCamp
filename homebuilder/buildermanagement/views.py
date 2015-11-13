from django.shortcuts import render
from django.views.generic import ListView
from viewsets import ModelViewSet
from .models import Project, Group, Contact, Room, Category, Item, AddOn

# Create your views here.
class GroupListView(ListView):
    model = Group


