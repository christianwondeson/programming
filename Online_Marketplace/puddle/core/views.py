from django.shortcuts import render, redirect
from item.models import Category, Item

from .forms import signupForm
# Create your views here. this are function based views that hand the content of the webpage based on the url route
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = signupForm()
    
    return render(request, 'core/signup.html',{
        'form': form,  
    })