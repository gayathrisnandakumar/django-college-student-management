from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
def home(request):
    return HttpResponse("Hello World")
@login_required(login_url='login')
def student_list(request):
    students=Student.objects.all().order_by('id')
    paginator=Paginator(students,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'students.html',{'students':page_obj})
def student_search(request):
    query=request.GET.get('q','')
    students=Student.objects.filter(name__icontains=query)
    return render(request,'students.html',{'students':students})
def student_add(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
            form=StudentForm()
    return render(request,'student_form.html',{'form':form})
def user_login(request):
    if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          user=authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('students')
          else:
               messages.error(request,'Invalid username or password')
    return render(request,'login.html')
def user_logout(request):
     logout(request)
     return redirect('login')