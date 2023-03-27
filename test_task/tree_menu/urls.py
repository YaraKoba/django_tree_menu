from django.urls import path
from .views import index, hello_page

urlpatterns = [
    path('<slug:menu_slug>/<slug:menu_item_slug>/', index, name='menu'),
    path('', hello_page, name='hello_page')
]
