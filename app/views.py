from django.shortcuts import render
# Create your views here.

def ifcondition(request):
    return render(request,'if.html',context={'data':'Hai','data1':'This is Saravanan'})

def forloop(request):
    return render(request,'for.html',context={'data':'Hai Saran'})

def image(request):
    return render(request,'image.html')


