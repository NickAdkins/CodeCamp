from django import forms
from .models import Room, Project, Contact

class RoomForm(forms.ModelForm):
   class Meta:
       model = Room 
       fields = ['name', 'project', 'sqfootage']

   def __init__(self, request, *args, **kwargs):
      super(RoomForm, self).__init__(*args, **kwargs)
      self.fields['project'].queryset = Project.objects.filter(builder__user = request.user)
