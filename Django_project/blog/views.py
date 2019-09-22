from django.shortcuts import render
#from django.http import HttpResponse

posts=[
    {
        'author' : 'Saurav Joshi',
        'title' : 'Blog Post 1',
        'content' : '1st Post Content',
        'date_posted' : 'September 22,2019',
    },
    {
        'author' : 'Arya Joshi',
        'title' : 'Blog Post 2',
        'content' : '2nd Post Content',
        'date_posted' : 'September 23,2019',
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
# Create your views here.
