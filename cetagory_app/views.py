from django.shortcuts import render,redirect
from cetagory_app.forms import Cetagory_form
# Create your views here.
def cetagory(request):
    if request.method == 'POST':
        form = Cetagory_form(request.POST)
        if form.is_valid():
        
            form.save()
            return redirect('show_task')
    else:
        form = Cetagory_form()
        
    return render(request,'cetagory.html',{'form':form})