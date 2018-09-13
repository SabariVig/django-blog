from django.shortcuts import render
from .models import Post
# Create your views here.

insert = {
    'posts': Post.objects.all(), 'title': "Home"
}


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return ip


def index(request):
    my_dict = {'insert_me': "Welcome TO Blog Page"}
    get_ip(request)
    return render(request, 'blog/index.html', context=insert)


def about(request):
    my_dict = {'insert_me': "Welcome To About Page", "title": "About"}
    return render(request, 'blog/about.html', context=my_dict)
