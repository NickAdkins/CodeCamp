from django.shortcuts import render
from django.views.generic import ListView
from viewsets import ModelViewSet
from .models import Project, Group, Contact, Room, Category, Item, AddOn

# Create your views here.
class GroupListView(ListView):
    model = Group

# Contact Views #

class ContactListView(ListView):
    models = Contact

#class ContactDetailView(DetailView):
#    models Contact
#
#class ContactCreateView(CreateView):
#    models Contact
#    success_url = reverse_lazy('bm:contact_list.html')
#    success_message = "%(name)s was created successfully"
#
#class ContactUpdateView(UpdateView):
#    models Contact
#    success_url = reverse_lazy('bm:contact_list.html')
#    success_message = "%(name)s was created successfully"
#
#class ContactDeleteView(DeleteView):
#    models Contact
#    success_url = reverse_lazy('bm:contact_list.html')
#    success_message = "%(name)s was created successfully"
#
## Project Views #
#
#class ProjectListView(ListView):
#    models = Project
#
#class ProjectDetailView(DetailView):
#    models Project
#
#class ProjectCreateView(CreateView):
#    models Project
#    success_url = reverse_lazy('bm:project_list.html')
#    success_message = "%(name)s was created successfully"
#
#class ProjectUpdateView(UpdateView):
#    models Project
#    success_url = reverse_lazy('bm:project_list.html')
#    success_message = "%(name)s was created successfully"
#
#class ProjectDeleteView(DeleteView):
#    models Project
#    success_url = reverse_lazy('bm:project_list.html')
#    success_message = "%(name)s was created successfully"
#
## Item Views #
#
#class ItemListView(ListView):
#    models = Item
#
#class ItemDetailView(DetailView):
#    models Item
#
#class ItemCreateView(CreateView):
#    models Item
#    success_url = reverse_lazy('bm:item_list.html')
#    success_message = "%(name)s was created successfully"
#
#class ItemUpdateView(UpdateView):
#    models Item
#    success_url = reverse_lazy('bm:item_list.html')
#    success_message = "%(name)s was updated successfully"
#
#class ItemDeleteView(DeleteView):
#    models Item
#    success_url = reverse_lazy('bm:item_list.html')
#    success_message = "%(name)s was deleted successfully"
