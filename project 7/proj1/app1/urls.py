from django.urls import path
from . import views

urlpatterns=[
    path('view',views.Viewfun),
    path('home',views.home),
    path('about',views.about)
]