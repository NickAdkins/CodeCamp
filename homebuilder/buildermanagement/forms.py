from django import forms
from .models import Room, Project, Contact, Category
from django.db.models import Q

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
      self.fields['project'].queryset = Project.objects.filter(builder__user = request.user)

class CategoryForm(forms.ModelForm):
   class Meta:
       model = Category 
       fields = ['name', 'project']

   def __init__(self, request, *args, **kwargs):
      super(CategoryForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(builder__user = request.user)
