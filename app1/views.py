from django.shortcuts import render

# Create your views here.


def images(request):
    return render(request,'index.html')