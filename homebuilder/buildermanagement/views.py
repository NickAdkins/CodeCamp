from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project, Group, Contact, Room, Category, Item, AddOn

# Create your views here.
class GroupListView(ListView):
    model = Group
    def get_queryset(self):
        return Group.objects.filter(user = self.request.user)

class GroupDetailView(DetailView):
    model = Group

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Group.objects.filter(user = self.request.user)


class GroupCreateView(SuccessMessageMixin, CreateView):
    model = Group
    success_url = reverse_lazy('bm:group_list')
    success_message = "Group %(name)s created successfully!"
    fields = ['name']

    def form_valid(self, form):
        # Set the user
        group = form.save(commit=False)
        group.user = self.request.user
        return super(GroupCreateView, self).form_valid(form)

class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    success_url = reverse_lazy('bm:group_list')
    success_message = "Group %(name)s updated successfully!"
    fields = ['name']

class GroupDeleteView(SuccessMessageMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('bm:group_list')
    success_message = "Group %(name)s deleted successfully!"


# Project Views #

class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(builder__user = self.request.user)

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'plansfile', 'address', 'budget', 'buyer']
    success_url = reverse_lazy('bm:project_list')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        # Set the builder
        project = form.save(commit=False)
        project.builder = Contact.objects.get(user = self.request.user)
        return super(ProjectCreateView, self).form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'plansfile', 'address', 'budget', 'buyer']
    success_url = reverse_lazy('bm:project_list')
    success_message = "%(name)s was update successfully"

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('bm:project_list')
    success_message = "%(name)s was deleted successfully"
