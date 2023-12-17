from django.shortcuts import render,redirect
from django.http import FileResponse
from django.views.generic import ListView ,DetailView
from .models import Menu_i
# Create your views here.
def home(request):
    return render(request,'menu/home.html')

def menu_item(request,item):
    data = {'item':item}
    return render(request,'menu/menu_item.html',data)


class SelectedItem(DetailView):
    model = Menu_i
    template_name = "menu/menu_item.html"

def about(request):
    return render(request,'menu/about.html')

class MenuView(ListView):
    model = Menu_i
    template_name = 'menu/menu_list.html'
    
def upload(request,file):
    img = open('uploads/'+file, 'rb')

    response = FileResponse(img)

    return response
    return redirect("https://127.0.0.1:8000/menu/uploads/"+file)