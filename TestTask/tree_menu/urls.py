from django.urls import path
from .views import index

urlpatterns = [
    path('<int:menu_id>/<int:menu_item_id>/', index, name='menu'),
]