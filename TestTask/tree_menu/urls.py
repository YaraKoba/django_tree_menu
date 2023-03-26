from django.urls import path
from .views import index

urlpatterns = [
    path('<slug:menu_slug>/<slug:menu_item_slug>/', index, name='menu'),
]