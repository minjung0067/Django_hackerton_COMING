from django.shortcuts import render
from django.http import HttpResponse
from .models import item


def main(request):
    Item = item.objects
    return render(request,'main.html',{"main_key":Item})

def newitem(request):
    New = new.objects
    return render(request,'newitem.html',{"new_key":New})

# Create your views here.
