from django.shortcuts import render, redirect


def index(request, *args, **kwargs):
    return render(request, 'tree_menu/index.html')



# Create your views here.
