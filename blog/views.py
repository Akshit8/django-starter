from django.shortcuts import render


posts = [
    {
        'author': 'Akshit',
        'title': 'Python django',
        'content': 'django is heavy framework',
        'date_posted': 'June 13, 2021'
    },
    {
        'author': 'Akshit',
        'title': 'Golang mux',
        'content': 'Golang mux is fast and lightweight',
        'date_posted': 'June 14, 2021'
    },
    {
        'author': 'Akshit',
        'title': 'Nodejs express',
        'content': 'express is best',
        'date_posted': 'June 15, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
