from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

def home(request):
  wish_list = Item.objects.all()
  return render(request, 'home.html', {
     'wish_list':wish_list
  })

def add(request):
    return render(request, 'add.html')


class ItemCreate(CreateView):
  model = Item
  fields = ['description']


class ItemDelete(DeleteView):
  model = Item
  success_url = '/'