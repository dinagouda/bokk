from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from bokk import models
from django.conf import settings
from bokk import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login


# Create your views here.
def Home(request):

    context={}
    return render(request, 'Home.html', context)


def signup_view(request):
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('Home')
    else:
        form=UserCreationForm()
    return render(request,'signup_view.html',{'form':form})


def login_view(request):
    if request.method =='POST':
      form=AuthenticationForm(data=request.POST)
      if form.is_valid():
          user=form.get_user()
          login(request,user)
          return redirect('Home')
    else:
        form=AuthenticationForm()


    return render(request,'login_view.html',{'formin':form})





def Children(request):
    children = models.children.objects.all()
    context = {'children': children}
    return render(request, 'Children.html', context)

def Political(request):
    Political= models.political.objects.all()
    context = {'Political': Political}
    return render(request, 'Political.html', context)

def Poetry(request):
    Poetry = models.poetry.objects.all()
    context = {'Poetry': Poetry}
    return render(request, 'Poetry.html', context)

def ArtDesign(request):
    ArtDesign = models.artdesign.objects.all()
    context = {'ArtDesign': ArtDesign}
    return render(request, 'Art&Design.html', context)

def Programing(request):
    Programing = models.programing.objects.all()
    context = {'Programing': Programing}
    return render(request, 'Programing.html', context)