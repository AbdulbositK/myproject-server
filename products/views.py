from django.shortcuts import render

# Create your views here.
# Контроллеры = views (выюхи) = function

def index(request):
    context = {
        'title' : 'Store'
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title' : 'Store - Каталог'
    }
    return render(request, 'products/products.html', context)