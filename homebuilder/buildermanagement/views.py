from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Project, Group, Contact, Room, Category, Item, AddOn, Phase
from .forms import RoomForm, CategoryForm, ItemForm, ContactForm, PhaseForm, AddOnForm

# Create your views here.
"""
    Groups
"""
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

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('bm:group_list')
    success_message = "Group deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GroupDeleteView, self).delete(request, *args, **kwargs)

"""
    Project
"""

class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(
            Q(builder__user = self.request.user) |
            Q(buyer__user = self.request.user)
        )


class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    fields = ['name', 'plansfile', 'address', 'budget', 'buyer']
    success_url = reverse_lazy('bm:project_list')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        # Set the builder
        project = form.save(commit=False)
        if 'plansfile' in self.request.FILES:
            project.plansfile = self.get_form_kwargs().get('files')['plansfile']
            project.save()
        project.builder = Contact.objects.get(user = self.request.user)
        return super(ProjectCreateView, self).form_valid(form)

class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    fields = ['name', 'plansfile', 'address', 'budget', 'buyer']
    success_url = reverse_lazy('bm:project_list')
    success_message = "%(name)s was update successfully"

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('bm:project_list')
    success_message = "Project deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)

"""
   Category
"""

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

"""
    Rooms
"""
class RoomListView(ListView):
    model = Room

    def get_queryset(self):
        return Room.objects.filter(
            Q(project__builder__user = self.request.user) |
            Q(project__buyer__user = self.request.user)
        ).order_by('project')

class RoomDetailView(DetailView):
    model = Room

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Room.objects.filter(user = self.request.user)


class RoomCreateView(SuccessMessageMixin, CreateView):
    model = Room
    success_url = reverse_lazy('bm:room_list')
    success_message = "Room %(name)s created successfully!"
    form_class = RoomForm

    def get_form_kwargs(self):
        kwargs = super(RoomCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class RoomUpdateView(SuccessMessageMixin, UpdateView):
    model = Room
    success_url = reverse_lazy('bm:room_list')
    success_message = "Room %(name)s updated successfully!"
    form_class = RoomForm

    def get_form_kwargs(self):
        kwargs = super(RoomUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class RoomDeleteView(SuccessMessageMixin, DeleteView):
    model = Room
    success_url = reverse_lazy('bm:room_list')
    success_message = "Room %(name)s deleted successfully!"

"""
    Items
"""
class ItemListView(ListView):
    model = Item

    def get_queryset(self):
        return Item.objects.filter(
            Q(project__builder__user = self.request.user) |
            Q(project__buyer__user = self.request.user)
        ).order_by('project')

class ItemDetailView(DetailView):
    model = Item

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Item.objects.filter(
            Q(project__builder__user = self.request.user) |
            Q(project__buyer__user = self.request.user)
        )


class ItemCreateView(SuccessMessageMixin, CreateView):
    model = Item
    success_url = reverse_lazy('bm:item_list')
    success_message = "Item %(material)s created successfully!"
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ItemUpdateView(SuccessMessageMixin, UpdateView):
    model = Item
    success_url = reverse_lazy('bm:item_list')
    success_message = "Item %(material)s updated successfully!"
    form_class = ItemForm

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ItemDeleteView(SuccessMessageMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('bm:item_list')
    success_message = "Item %(material)s deleted successfully!"

   ######AddOn#######

class AddOnListView(ListView):
    model = AddOn

    def get_queryset(self):
        return AddOn.objects.filter(
            Q(item__project__builder__user = self.request.user) |
            Q(item__project__buyer__user = self.request.user)
        )#.order_by('project')

class AddOnDetailView(DetailView):
    model = AddOn

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return AddOn.objects.filter(
            Q(item__project__builder__user = self.request.user) |
            Q(item__project__buyer__user = self.request.user)
        )


class AddOnCreateView(SuccessMessageMixin, CreateView):
    model = AddOn
    success_url = reverse_lazy('bm:addon_list')
    success_message = "AddOn %(item_description)s created successfully!"
    form_class = AddOnForm

    def get_form_kwargs(self):
        kwargs = super(AddOnCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class AddOnUpdateView(SuccessMessageMixin, UpdateView):
    model = AddOn
    success_url = reverse_lazy('bm:addon_list')
    success_message = "AddOn %(item_description)s updated successfully!"
    form_class = AddOnForm

    def get_form_kwargs(self):
        kwargs = super(AddOnUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class AddOnDeleteView(SuccessMessageMixin, DeleteView):
    model = AddOn
    success_url = reverse_lazy('bm:addon_list')
    success_message = "AddOn %(item_description)s deleted successfully!"

"""
    Contacts
"""
class ContactListView(ListView):
    model = Contact

    def get_queryset(self):
        return Contact.objects.filter(group__user = self.request.user).order_by('name')

class ContactDetailView(DetailView):
    model = Contact

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Contact.objects.filter(group__user = self.request.user)


class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    success_url = reverse_lazy('bm:contact_list')
    success_message = "Contact %(name)s created successfully!"
    form_class = ContactForm

    def get_form_kwargs(self):
        kwargs = super(ContactCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ContactUpdateView(SuccessMessageMixin, UpdateView):
    model = Contact
    success_url = reverse_lazy('bm:contact_list')
    success_message = "Contact %(name)s updated successfully!"
    form_class = ContactForm

    def get_form_kwargs(self):
        kwargs = super(ContactUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ContactDeleteView(SuccessMessageMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('bm:contact_list')
    success_message = "Contact %(name)s deleted successfully!"

"""
    Phases
"""
class PhaseListView(ListView):
    model = Phase

    def get_queryset(self):
        return Phase.objects.filter(
            Q(project__builder__user = self.request.user) |
            Q(project__buyer__user = self.request.user)
        )

class PhaseDetailView(DetailView):
    model = Phase

    # Make it so that users don't see objects that belong to someone else
    def get_queryset(self):
        return Phase.objects.filter(
            Q(project__builder__user = self.request.user) |
            Q(project__buyer__user = self.request.user)
        )


class PhaseCreateView(SuccessMessageMixin, CreateView):
    model = Phase
    success_url = reverse_lazy('bm:phase_list')
    success_message = "Phase %(name)s created successfully!"
    form_class = PhaseForm

    def get_form_kwargs(self):
        kwargs = super(PhaseCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class PhaseUpdateView(SuccessMessageMixin, UpdateView):
    model = Phase
    success_url = reverse_lazy('bm:phase_list')
    success_message = "Phase %(name)s updated successfully!"
    form_class = PhaseForm

    def get_form_kwargs(self):
        kwargs = super(PhaseUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class PhaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Phase
    success_url = reverse_lazy('bm:phase_list')
    success_message = "Phase %(name)s deleted successfully!"
    
""" 
Home Page Views
"""

class BuilderView(TemplateView):
    template_name = 'buildermanager/builder_home.html'

    def get_context_data(self, **kwargs):
        context = super(BuilderView, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.filter(builder__user = self.request.user)
        context['contact_list'] = Contact.objects.filter(group__user = self.request.user)
        return context

class BuyerView(TemplateView):
    template_name = 'buildermanager/builder_home.html'

class SubcontractorView(TemplateView):
    template_name = 'buildermanager/builder_home.html'

class HomePageView(View):

    builder_view = staticmethod(BuilderView.as_view())
    buyer_view = staticmethod(BuyerView.as_view())
    subcontractor_view = staticmethod(SubcontractorView.as_view())

    def dispatch(self, request, *args, **kwargs):
        if Project.objects.get(builder__user = request.user)[0]:
            return self.builder_view(request, *args, **kwargs)
        elif Project.objects.get(buyer__user = request.user)[0]:
            return self.buyer_view(request, *args, **kwargs)
        else:
            return self.subcontractor_view(request, *args, **kwargs)

