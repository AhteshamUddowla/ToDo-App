from django.forms import ModelForm
from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={'placeholder': 'Enter new task here...'})
        }
    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'id': 'todo-input'})