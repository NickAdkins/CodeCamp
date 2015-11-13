from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project, Group, Contact, Room, Category, Item, AddOn
from .forms import RoomForm, CategoryForm

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
    
class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(project__builder__user = self.request.user)

class CategoryDetailView(DetailView):
    model = Category 
    
    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category 
    success_url = reverse_lazy('bm:category_list')
    success_message = "Category %(name)s created successfully!"
    form_class = CategoryForm

    def get_form_kwargs(self):
        kwargs = super(CategoryCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category 
    success_url = reverse_lazy('bm:category_list')
    success_message = "Category %(name)s updated successfully!"
    form_class = CategoryForm
 
    def get_form_kwargs(self):
        kwargs = super(CategoryUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category 
    success_url = reverse_lazy('bm:category_list')
    success_message = "Category %(name)s deleted successfully!"
    
