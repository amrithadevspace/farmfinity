from django.shortcuts import render
from order.models import Order
from product.models import Product
import datetime
from order.models import Order
# Create your views here.

def order (request,idd):
    objj = Product.objects.get(product_id=idd)
    context = {
        "kk": objj
    }
    ss=request.session['u_id']

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        total = int(objj.price)*quantity
        obj=Order()
        obj.user_id=ss
        obj.product_id=idd
        obj.quantity=quantity
        obj.total_amount=total
        obj.status='pending'
        obj.date=datetime.datetime.today()
        obj.save()
        return render(request, 'order/successful.html')

    return render(request,'order/post order.html',context)

def manage_order(request):
    ss=request.session['u_id']
    obj =Order.objects.filter(product__farmer_id=ss)
    context = {
        "aa": obj
    }
    return render(request, 'order/manage order..html', context)
def view_order2 (request):
    obj =Order.objects.all()
    context = {
        "aa": obj
    }
    return render(request,'order/view order2.html',context)


def view_history(request):
    ss=request.session['u_id']
    obj = Order.objects.filter(user_id=ss)
    context = {
        "aa": obj
    }
    return render(request,'order/view history.html',context)

def accept(request,idd):
    obj=Order.objects.get(order_id=idd)
    obj.status='accepted'
    obj.save()
    return manage_order(request)

def reject(request,idd):
  obj=Order.objects.get(order_id=idd)
  obj.status='rejected'
  obj.save()
  return manage_order(request)