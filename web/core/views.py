from django.shortcuts import render
from .models import Contact,QuickMenu

# Create your views here.
def home(request):
    object = Contact.objects.all()
    object1= QuickMenu.objects.all()
    context = {'item':object,'quickmenus':object1}
    return render(request,'home.html',context=context)

def test(request):
    return render(request,'test.html')