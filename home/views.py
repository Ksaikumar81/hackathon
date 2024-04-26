import sx
from django.contrib import messages
from django.shortcuts import render, redirect
from requests import auth

from .models import customerdetail, transactiondetail  # Added the necessary import

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'NewHomePage.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def customers(request):
    customers = customerdetail.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except:
            print("enter amount")
        for i in customers:
            print(email)
            if i.email == email:
                j = i
                id = i.id
                break
        for i in customers:
            print(i.email, i.avail_bal, semail)
            if i.email == semail and amt < i.avail_bal and amt > 0:
                avail_bal = i.avail_bal - amt
                avail_bal2 = j.avail_bal + amt
                try:
                    query1 = transactiondetail(name=i.name, email=i.email,  # Changed to TransactionDetail
                                               deb_amt=amt, cr_amt=0, ac_bal=avail_bal)

                    query2 = customerdetail(  # Changed to CustomerDetail
                        id=i.id, avail_bal=avail_bal, email=i.email, name=i.name)
                    query3 = transactiondetail(name=j.name, email=j.email,  # Changed to TransactionDetail
                                               deb_amt=0, cr_amt=amt, ac_bal=avail_bal2)
                    query4 = customerdetail(  # Changed to CustomerDetail
                        id=id, avail_bal=avail_bal2, email=j.email, name=j.name)
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()

                    return redirect('/customers')

                    break
                except:
                    print("transaction failed")
                    break
        else:
            print("invalid data")

    return render(request, 'customers.html', {'customers': customers})


def payment(request):
    customers = customerdetail.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except:
            print("enter amount")
        for i in customers:
            print(email)
            if i.email == email:
                j = i
                id = i.id
                break
        for i in customers:
            print(i.email, i.avail_bal, semail)
            if i.email == semail and amt < i.avail_bal and amt > 0:
                avail_bal = i.avail_bal - amt
                avail_bal2 = j.avail_bal + amt
                try:
                    query1 = transactiondetail(name=i.name, email=i.email,  # Changed to TransactionDetail
                                               deb_amt=amt, cr_amt=0, ac_bal=avail_bal)

                    query2 = customerdetail(  # Changed to CustomerDetail
                        id=i.id, avail_bal=avail_bal, email=i.email, name=i.name)
                    query3 = transactiondetail(name=j.name, email=j.email,  # Changed to TransactionDetail
                                               deb_amt=0, cr_amt=amt, ac_bal=avail_bal2)
                    query4 = customerdetail(  # Changed to CustomerDetail
                        id=id, avail_bal=avail_bal2, email=j.email, name=j.name)
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()

                    return redirect('/customers')

                    break
                except:
                    print("transaction failed")
                    break
        else:
            print("invalid data")

    return render(request, 'payment.html')


def trans(request):
    transactions = transactiondetail.objects.all()  # Changed to TransactionDetail
    return render(request, 'trans.html', {'transactions': transactions})


def contact(request):
    return render(request, 'contact.html')
