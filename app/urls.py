from django.urls import path,include
from . import views

urlpatterns = [
   # path("",views.Indexview,name="index"),
   path("",views.HTMLFORM,name="htmlform"),
]