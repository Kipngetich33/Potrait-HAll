from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def welcome(request):
    message= "Test"
    return render(request,'all-pics/all_pics.html')