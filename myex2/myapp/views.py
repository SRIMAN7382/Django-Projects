from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return render(request,"2.html",{})

# Create your views here.
