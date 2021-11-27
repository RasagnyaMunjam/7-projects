from django.shortcuts import render,HttpResponse

# Create your views here.
def basic(request):
    return HttpResponse("this is wgl")