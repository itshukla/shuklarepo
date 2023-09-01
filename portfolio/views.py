from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .form import *
def port(request):
    return render(request,'index.html')
# Create your views here.


def create(request):
    fm = userForm()
    if request.method == 'POST':
        fm = userForm(request.POST)
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        subject = request.POST.get('subject'),
        message = request.POST.get('message'),
        if fm.is_valid():
            fm.save()
        #     return redirect('port')
        
    else:
        pass
    return render(request,'index.html',{'form':fm})
