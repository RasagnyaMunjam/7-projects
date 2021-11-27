from django.shortcuts import render,HttpResponse


# Create your views here.
def viewfunc(request):
    return HttpResponse("this is banagalore")