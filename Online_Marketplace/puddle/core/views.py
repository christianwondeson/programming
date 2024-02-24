from django.shortcuts import render


# Create your views here. this are function based views that hand the content of the webpage based on the url route
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')