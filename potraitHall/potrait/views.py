from django.http  import HttpResponse
from django.shortcuts import render

# Views will be created here
def welcome(request):
    message= "Test"
    return render(request,'all-pics/all_pics.html',{"message":message,}) 