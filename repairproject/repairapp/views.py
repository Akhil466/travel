from django.http import HttpResponse
from django.shortcuts import render
from . models import Edit,team


# Create your views here.
def demo(request):
    obj=Edit.objects.all()
    return render(request,"index.html",{'result':obj})

def Team(request):
    obj2=team.objects.all()
    return render(request,"index.html",{'result2':obj2})