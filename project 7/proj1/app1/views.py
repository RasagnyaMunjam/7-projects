from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def Viewfun(request):
    context = modelclass.objects.all()
    return render(request, "Viewfun.html", {'con': context})


def home(request):
    context={'city':"hyderabad",'year':2021}
    return render(request, "home.html",context)


def about(request):
    return render(request, "about.html",{"name":"rasu"})
