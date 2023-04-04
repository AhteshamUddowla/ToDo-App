from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo
from .forms import ToDoForm

# Create your views here.
def createToDo(request):
    todos = ToDo.objects.all()
    form = ToDoForm()

    if request.method == 'POST':    
        form = ToDoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'todos': todos, 'form':form}
    return render(request, 'main.html', context)

# def createToDo(request):
#     print("Hello1")
#     if request.method == 'POST':    
#         form = ToDoForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        

def updateToDo(request, pk):
    todos = ToDo.objects.all()
    todo = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=todo)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'todos':todos, 'todo':todo, 'form':form}
    return render(request, 'main.html', context)



def deleteToDo(request,pk):
    todo = ToDo.objects.get(id=pk)

    todo.delete()
    return redirect('todo')
    
