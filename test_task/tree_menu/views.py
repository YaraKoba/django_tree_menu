from django.shortcuts import render, reverse


def index(request, *args, **kwargs):

    # В зависимости от текущего url отправляем нужный шаблон страницы
    if request.path == '/main_menu/home/':
        file = 'example_pages/home.html'
    elif request.path == '/main_menu/contact/':
        file = 'example_pages/contact.html'
    elif request.path == '/main_menu/about/':
        file = 'example_pages/about.html'
    else:
        file = 'example_pages/any.html'

    return render(request, file)


# Отправляем шаблон для первой страницы
def hello_page(request, *args, **kwargs):
    return render(request, 'tree_menu/index.html')
