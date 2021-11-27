from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    a="welcome to 301"
    return HttpResponse(a)
