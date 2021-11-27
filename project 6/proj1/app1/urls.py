from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('fariha',views.admin),
    path('salman',views.about)
]