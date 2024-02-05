from django.shortcuts import render


# dummy data for our blog post template
posts=[
    {
        "author":"CoreyMs",
        "title":"Blog Post 1",
        "content":"First post content",
        'date_posted':"august 27, 2018",
    },
    {
        "author":"jane Doe",
        "title":"Blog Post 2",
        "content":"second post content",
        'date_posted':"august 28, 2018",
    },
]

# Create your views here.
def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {"title": "About"})