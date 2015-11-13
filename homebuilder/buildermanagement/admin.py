from django.contrib import admin

from .models import Group, Category, Room, Contact, Item, AddOn, Project, Phase

# Register your models here.

admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Contact)
admin.site.register(Item)
admin.site.register(AddOn)
admin.site.register(Project)
admin.site.register(Phase)
