from django.forms import ModelForm
from .models import Task

# creating a form 
class TaskForm(ModelForm):

	class Meta:
		model = Task
		fields = '__all__'
