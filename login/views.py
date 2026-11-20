from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Login
from farmer.models import Farmer
from krishibhavan.models import Krishibhavan


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        obj = Login.objects.filter(username=username, password=password)

        if obj.exists():

            for ob in obj:

                uid = ob.u_id
                tp = ob.type

                if tp == "admin":
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/admin/')

                elif tp == "user":
                    request.session["u_id"] = uid
                    return HttpResponseRedirect('/temp/user/')

                elif tp == "farmer":

                    farmer = Farmer.objects.get(farmer_id=uid)

                    if farmer.status == "accepted":
                        request.session["u_id"] = uid
                        return HttpResponseRedirect('/temp/farmer/')

                    else:
                        return render(request, "login/login.html",
                                      {"msg": "Your account is waiting for admin approval."})

                elif tp == "krishibhavan":
                     request.session["u_id"] = uid
                     return HttpResponseRedirect('/temp/krishibhavan/')

            else:
                        return render(request, "login/login.html",
                                      {"msg": "Your account is waiting for admin approval."})

        else:

            return render(request, "login/login.html",
                          {"msg": "Invalid username or password."})

    return render(request, "login/login.html")