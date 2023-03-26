from django.shortcuts import render, redirect


def index(request, *args, **kwargs):
    if request.path == '/main_menu/home/':
        file = 'example_pages/home.html'
    elif request.path == '/main_menu/contact/':
        file = 'example_pages/contact.html'
    elif request.path == '/main_menu/about/':
        file = 'example_pages/about.html'
    else:
        file = 'tree_menu/index.html'
    return render(request, file)


def hello_page(request, *args, **kwargs):
    pass
