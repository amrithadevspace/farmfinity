from django.shortcuts import render
from product.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializer import ProductSerializer
import datetime
from  django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
# Create your views here.

def product (request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Product()
        obj.farmer_id=ss
        obj.date=datetime.datetime.today()
        obj.product_name=request.POST.get('product_name')
        # obj.photo=request.POST.get('photo')
        myfile = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        obj.photo = myfile.name
        obj.category=request.POST.get('category')
        obj.description=request.POST.get('description')
        obj.price = request.POST.get('price')
        obj.unit = request.POST.get('unit')
        obj.quantity= request.POST.get('quantity')
        obj.save()

    return render(request,'product/post product.html')

from .models import Product, Wishlist

def view_product(request):

    uid = request.session['u_id']

    products = Product.objects.all()

    wish = Wishlist.objects.filter(user_id=uid)

    wishlist_ids = []

    for i in wish:
        wishlist_ids.append(i.product_id)

    context = {
        "aa": products,
        "wishlist_ids": wishlist_ids
    }

    return render(request, 'product/view product.html', context)
from django.shortcuts import render
from .models import Product

def view_product2(request):

    obj = Product.objects.all()

    context = {
        "aa": obj
    }

    return render(request, 'product/view product details2.html', context)
from django.http import JsonResponse

def product_search(request):

    search = request.GET.get('search', '')

    if search:
        products = Product.objects.filter(
            product_name__icontains=search
        )
    else:
        products = Product.objects.all()

    uid = request.session['u_id']

    wish = Wishlist.objects.filter(user_id=uid)

    wishlist_ids = []

    for i in wish:
        wishlist_ids.append(i.product_id)

    data = []

    for i in products:

        farmer_name = ""

        try:
            farmer_name = i.farmer.farmer_name
        except:
            farmer_name = ""

        data.append({
            'product_id': i.product_id,
            'product_name': i.product_name,
            'category': i.category,
            'description': i.description,
            'price': i.price,
            'quantity': i.quantity,
            'unit': i.unit,
            'photo': str(i.photo),
            'farmer_name': farmer_name,
        })

    return JsonResponse({
        'products': data,
        'wishlist_ids': wishlist_ids
    })
def update(request,idd):
    ss = request.session['u_id']
    obj=Product.objects.get(product_id=idd)
    context={
        "k":obj
    }
    if request.method=='POST':
     obj=Product.objects.get(product_id=idd)
     obj.farmer_id=ss
     obj.date=datetime.datetime.today()
     obj.product_name=request.POST.get('product name')
     obj.photo = request.POST.get('photo')
     obj.category = request.POST.get('category')
     obj.description = request.POST.get('description')
     obj.price = request.POST.get('price')
     obj.unit = request.POST.get('unit')
     obj.quantity = request.POST.get('quantity')
     obj.save()
    return  render(request,'product/update.html',context)

def view_update(request):
    obj=Product.objects.all()
    context={
        'k':obj
    }
    return render(request,'product/view_update.html',context)


def addto_wishlist(request, idd):

    uid = request.session['u_id']

    obj = Wishlist.objects.filter(user_id=uid, product_id=idd)

    if obj.exists():
        obj.delete()
    else:
        wish = Wishlist()
        wish.user_id = uid
        wish.product_id = idd
        wish.save()

    return HttpResponseRedirect('/product/v_prod/')
from django.shortcuts import render
from .models import Wishlist, Product

def view_wishlist(request):

    uid = request.session['u_id']

    wish = Wishlist.objects.filter(user_id=uid)

    products = []

    for i in wish:

        product = Product.objects.get(product_id=i.product_id)

        products.append(product)

    return render(request, 'product/wishlist.html', {'aa': products})
from django.http import HttpResponseRedirect

def remove_wishlist(request, idd):

    uid = request.session['u_id']

    obj = Wishlist.objects.filter(
        user_id=uid,
        product_id=idd
    )

    obj.delete()

    return HttpResponseRedirect('/product/v_wishlist/')


class ProductList(APIView):
    def get(self,request):
        Products=Product.objects.all()
        serializer=ProductSerializer(Products,many=True)
        return Response(serializer.data)

    def post(self, request):

        farmer_id = request.data['farmer_id']
        date = request.data['date']
        product_name = request.data['product_name']
        photo = request.data['photo']
        category = request.data['category']
        description = request.data['description']
        price = request.data['price']
        quantity = request.data['quantity']
        unit = request.data['unit']

        product = Product.objects.create(
            farmer_id=farmer_id,
            date=date,
            product_name=product_name,
            photo=photo,
            category=category,
            description=description,
            price=price,
            quantity=quantity,
            unit=unit
        )

        return Response({
            'message': 'Product added successfully',
            'product_id': product.product_id,
            'product_name': product.product_name
        })

    def put(self, request, id):
        product = Product.objects.get(product_id=id)
        product.farmer_id = request.data['farmer_id']
        product.date = request.data['date']
        product.product_name = request.data['product_name']
        product.photo = request.data['photo']
        product.category = request.data['category']
        product.description = request.data['description']
        product.price = request.data['price']
        product.quantity = request.data['quantity']
        product.unit = request.data['unit']

        product.save()

        return Response({
            'message': 'Product updated successfully',
            'product_id': product.product_id,
            'product_name': product.product_name
        })

    def patch(self, request, id):
        product = Product.objects.get(product_id=id)

        if 'product_name' in request.data:
            product.product_name = request.data['product_name']

        product.save()

        return Response({
            'message': 'Product partially updated successfully',
            'product_id': product.product_id,
            'product_name': product.product_name
        })



    def delete(self, request, id):
            product = Product.objects.get(product_id=id)

            product.delete()

            return Response({
                'message': 'Product deleted successfully',
                'product_id': id
            })