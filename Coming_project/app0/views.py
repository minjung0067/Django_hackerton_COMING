from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import item,new,category
from django.contrib import auth


def main(request):
    Item = item.objects
    return render(request,'main.html',{"main_key":Item})

def newitem(request):
    New = new.objects
    return render(request,'newitem.html',{"new_key":New})
def home(request):
    return render(request,'home.html')

def loginhome(request):
    return render(request,'loginhome.html')

def signuphome(request):
    return render(request,'signuphome.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            errormasg ="잘못입력하셨습니다"
            return render(request, 'loginhome.html',{'errormasg':errormasg})
    else:
        return redirect('loginhome.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signuphome.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
# def category(request):
#     Cate = category.objects
#     return render(request,'')

# Create your views here.
