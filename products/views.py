from django.shortcuts import render

# Create your views here.
# Контроллеры = views (выюхи) = function

def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать',
        'username': 'Abdulbosit kabilov'
    }
    return render(request, 'products/test-context.html', context)
