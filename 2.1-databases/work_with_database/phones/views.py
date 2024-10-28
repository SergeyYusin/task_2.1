from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = str(request.GET.get("sort", "name"))
    template = 'catalog.html'
    if sort_by == "name":
        phones_all = Phone.objects.order_by('name')
    elif sort_by == "min_price":
        phones_all = Phone.objects.order_by('price')
    elif sort_by == "max_price":
        phones_all = Phone.objects.order_by('-price')
    else:
        phones_all = Phone.objects.all()
    context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
