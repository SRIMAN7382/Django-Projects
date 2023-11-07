from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    msg1='<h1>HI HELLO WELCOME TO DJANGO</h1>'
    return HttpResponse(msg1)
def view2(request):
    msg2='<h2>HI WELCOME TO PYTHON CLASS</h2>'
    return HttpResponse(msg2)


# Create your views here.
