from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    
    return render(request,"home.html",{})

# Create your views here.
