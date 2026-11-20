from django.shortcuts import render,redirect
from payment.models import Payment
from order.models import Order
from product.models import Product
import datetime


# Create your views here.

def payment(request,idd):
    objj =Order.objects.get(order_id=idd)
    context = {
        "kk": objj
    }

    if request.method=='POST':
        obj=Payment()
        obj.order_id=idd
        obj.amount=objj.total_amount
        obj.payment_method=request.POST.get('select')
        obj.status='paid'
        obj.date=datetime.datetime.today()
        obj.save()
        return redirect('/order/v_history/')
    return render(request,'payment/payment.html',context)

def  view_payment(request):
    # ss=request.session['u_id']
    objj =Payment.objects.all()
    context = {
        "aa": objj
    }
    return render(request,'payment/view payment.html',context)
