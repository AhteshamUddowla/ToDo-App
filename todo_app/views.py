from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile, ToDo
from .forms import ProfileForm, ToDoForm, CustomUserCreationForm

# Create your views here.
def registerUser(request):
    text = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account created successfully")
            login(request, user)
            return redirect('todo')
        else:
             messages.error(request, 'An error has occured')
        
    context = {'text': text, 'form':form}
    return render(request, 'register_login.html', context)

def loginUser(request):
    text = 'login'

    if request.user.is_authenticated:
        return redirect('todo')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            # print("Username doesn't exists")
            messages.error(request, "Username doesn't exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.error(request, 'Username or password is incorrect')
    

    context = {'text': text}
    return render(request, 'register_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userAccount(request,pk):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'account.html', context)

@login_required(login_url='login')
def editProfile(request, pk):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account', pk=profile.id)

    context = {'form':form}
    return render(request, 'edit_profile.html', context)

@login_required(login_url='login')
def createToDo(request):
    profile = request.user.profile
    todos = profile.todo_set.all()
    form = ToDoForm()

    if request.method == 'POST':    
        form = ToDoForm(request.POST)
        
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = profile
            todo.save()
            return redirect('todo')

    context = {'todos': todos, 'form':form}
    return render(request, 'todo_list_form.html', context)
        
@login_required(login_url='login')
def updateToDo(request, pk):
    profile = request.user.profile
    todos = profile.todo_set.all()
    todo = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=todo)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect('todo')
        
    context = {'todos':todos, 'todo':todo, 'form':form}
    return render(request, 'todo_list_form.html', context)


@login_required(login_url='login')
def deleteToDo(request,pk):
    todo = ToDo.objects.get(id=pk)

    if request.method=="POST":
        todo.delete()
        return redirect('todo')
    
    context = {'todo': todo}
    return render(request, 'delete_form.html', context)
    
