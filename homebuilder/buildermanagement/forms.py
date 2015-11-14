from django import forms
from django.db.models import Q
from .models import Room, Project, Contact, Item, Category, Contact, Group, Phase, AddOn

class RoomForm(forms.ModelForm):
   class Meta:
       model = Room 
       fields = ['name', 'project', 'sqfootage']

   def __init__(self, request, *args, **kwargs):
      super(RoomForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(
          Q(builder__user = request.user) |
          Q(buyer__user = request.user) 
      )

class ItemForm(forms.ModelForm):
   class Meta:
       model = Item
       fields = ['project', 'category', 'room', 'material', 'detail', 'cost', 'picture', 'picture_url', 'estimate_needed']

   def __init__(self, request, *args, **kwargs):
      super(ItemForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(
          Q(builder__user = request.user) |
          Q(buyer__user = request.user) 
      )
      self.fields['category'].queryset = Category.objects.filter(
          Q(project__builder__user = request.user) |
          Q(project__buyer__user = request.user) 
      )
      self.fields['room'].queryset = Room.objects.filter(
          Q(project__builder__user = request.user) |
          Q(project__buyer__user = request.user) 
      )

class CategoryForm(forms.ModelForm):
   class Meta:
       model = Category 
       fields = ['name', 'project']

   def __init__(self, request, *args, **kwargs):
      super(CategoryForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(
          Q(builder__user = request.user) |
          Q(buyer__user = request.user) 
      )

class AddOnForm(forms.ModelForm):
   class Meta:
       model = AddOn 
       fields = ['item', 'item_description', 'cost']

   def __init__(self, request, *args, **kwargs):
      super(AddOnForm, self).__init__(*args, **kwargs)
      self.fields['item'].queryset = Item.objects.filter(
          Q(project__builder__user = request.user) |
          Q(project__buyer__user = request.user) 
      )

class ContactForm(forms.ModelForm):
   class Meta:
       model = Contact
       fields = ['name', 'contact_type', 'group', 'email', 'address', 'phone1', 'phone2']

   def __init__(self, request, *args, **kwargs):
      super(ContactForm, self).__init__(*args, **kwargs)
      self.fields['group'].queryset = Group.objects.filter(user = request.user)

class PhaseForm(forms.ModelForm):
   class Meta:
       model = Phase
       fields = ['name', 'project', 'start_date', 'end_date', 'order_materials_by', 'depends_on', 'completed']

   def __init__(self, request, *args, **kwargs):
      super(PhaseForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(
            Q(builder__user = request.user) | 
            Q(buyer__user = request.user) 
        )
      if self.instance:
          self.fields['depends_on'].queryset = Phase.objects.exclude(pk=self.instance.pk)

