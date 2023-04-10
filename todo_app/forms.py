from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.forms.widgets import FileInput
from django import forms
from .models import Profile, ToDo


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your name...','autofocus': True}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email...'}),
            'password1': forms.PasswordInput(attrs={'placeholder': '••••••••••••••••'}),
            'password2': forms.PasswordInput(attrs={'placeholder': '••••••••••••••••'}),
        }
    
        

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'profile_image']
        # To remove clear checkbox of ImageField from form use the following line
        # Here 'form-control-file' is a Bootstrap class
        widgets = {
            'profile_image': FileInput(attrs={'class': 'form-control-file'}),
            # Username is not edit-able
            'username': forms.TextInput(attrs={'disabled': 'disabled'})
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


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