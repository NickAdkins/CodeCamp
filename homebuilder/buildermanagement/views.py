from django.shortcuts import render
from viewsets import ModelViewSet
from .models import Project, Group, Contact, Room, Category, Item, AddOn

# Create your views here.
class GroupViewSet(ModelViewSet):
    model = Group


