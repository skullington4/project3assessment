from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.ItemCreate.as_view(), name='add'),
    path('item/,<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]