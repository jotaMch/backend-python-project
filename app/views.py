from django.shortcuts import render, redirect
from app.forms import PratosForm
from app.models import Pratos
from django.core.paginator import Paginator

# Create your views here.

def products(request): 
    return render(request, 'products.html' )

def cart(request): 
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Pratos.objects.filter(prato__icontains=search)
    else:
        data['db'] = Pratos.objects.all()
        print(data, 'hello')
    
    total_price = sum(item.preco for item in data['db'])
    
    # Passa o total para o template
    data['total_price'] = total_price
    
    return render(request, 'cart.html', data)


def form(request):
    data= {}
    data['form'] = PratosForm()
    return render(request, 'form.html', data)

def create(request):
    form = PratosForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)  # Para verificar o que está sendo enviado
        if form.is_valid():
            form.save()
            return redirect('/')

def view(request, pk):
    data = {}
    data['db'] = Pratos.objects.get(pk=pk)
    return render(request,'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Pratos.objects.get(pk=pk)
    data['form'] = PratosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pratos.objects.get(pk=pk)
    form = PratosForm(request.POST or None, instance=data['db'])
    print(form)
    if form.is_valid():
        form.save()
    return redirect('cart')

def delete(request, pk):
    db = Pratos.objects.get(pk=pk)
    db.delete()
    return redirect('cart')

def production(request):
    data = {}
    data['db'] = Pratos.objects.all()
    print(data)
    return render(request, 'production.html', data)