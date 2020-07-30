from django.shortcuts import render
from django.http import HttpResponse

def child(request):
    return render(request,'child.html')
def home(request):
    return render(request,'myapp/home.html',{'name':'rana'})
def sam(request):
    return render(request,'myapp/sam.html')

# Create your views here.
