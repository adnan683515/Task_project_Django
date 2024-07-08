from django.shortcuts import render,redirect
from task_app.forms import task_form
from task_app import models
# Create your views here.
def taskForm(request):
    if request.method == 'POST':
        form = task_form(request.POST)
        if form.is_valid():
      
            form.save()
            return redirect('show_task')
            
    else:
        form = task_form()
    return render(request,'task.html',{'form':form})

def show_task(request):
    data = models.task.objects.all()
    return render(request,'show.html',{'data':data})


def edit(request,id):

    data = models.task.objects.get(pk=id)
    form = task_form(instance=data)
    if request.method=='POST':
        form = task_form(request.POST,instance=data)
        if form.is_valid():
            
            
            form.save()
            return redirect('show_task')
    
  
    return render(request,'task.html',{'form':form})


def delete(request,id):
    data = models.task.objects.get(pk=id)
    data.delete()
    return redirect('show_task')