from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import F
from django.http import HttpResponse
from datetime import datetime
from .models import FirstappModel
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .forms import LoginForm
from django.contrib.auth.models import auth

# Create your views here.
def home(request):
    # serverTime=datetime.now()
    # return render(request,'home.html',{'currentTime':serverTime})

    f=FirstappModel.objects.all()
    return render(request,'home.html',{'f':f})

def about(request):
    return render(request,'about.html')

def add(request):                                                                 
    n1=int(request.POST['n1'])
    n2=int(request.POST['n2'])
    result=n1+n2
    return render(request,'add.html',{'result':result})

def register(request):
        if request.method=="POST":
                form=UserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        username=form.cleaned_data.get('username')
                        messages.success(request,"Account created for "+username+"!")
                        return redirect('/register')
        else:
                form=UserCreationForm()
        return render(request,'register.html',{'form':form})

def login(request):
        if request.method=='GET':
                form=LoginForm()
                return render(request,"login.html",{"form":form})
        else:
                u1=request.POST["u"]
                p1=request.POST["p"]
                user=auth.authenticate(username=u1,password=p1)
                if user is not None:
                        auth.login(request,user)
                        return redirect("/")
                else:
                        messages.error(request,"invalid credentials")
                        return redirect("login")

def logout(request):
        auth.logout(request)
        return redirect("/")

class FirstappListView(ListView):
        model=FirstappModel
        template_name="home.html"
        context_object_name="f"

class FirstappCreateView(CreateView):
        model=FirstappModel
        template_name="form.html"
        fields="__all__"

class FirstappDetailView(DetailView):
        model=FirstappModel
        template_name="detail.html"

class FirstappUpdateView(UpdateView):
        model=FirstappModel
        template_name="form.html"
        fields="__all__"

class FirstappDeleteView(DeleteView):
        model=FirstappModel
        template_name="delconfirmmsg.html"
        success_url="/"