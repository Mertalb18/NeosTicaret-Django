from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

def home(request):
    products = Product.objects.all()

    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        products = Product.objects.filter(
            Q(productName__icontains = search)
        )

    context = {
        'products': products,
        'search': search
    }

    return render(request, "index.html", context)

def product(request, productId):
    product = Product.objects.filter(id = productId)
    print(product)

    context = {
        'product': product
    }
    return render(request, "product.html", context)

def create(request):
    if request.method == 'POST':
        productImage = request.FILES['resim']
        productName = request.POST['isim']
        productInfo = request.POST['aciklama']
        productPrice = request.POST['fiyat']

        urun = Product.objects.create(
            productImage = productImage,
            productName = productName,
            productInfo = productInfo,
            productPrice = productPrice
        )
        urun.save()
        print("Ürün oluşturuldu.")
        return redirect("create")

    return render(request, "create.html")
