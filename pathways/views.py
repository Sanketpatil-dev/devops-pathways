from django.shortcuts import render
from pathways.models import contactus, bookticket, signup
from datetime import datetime

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def destination(request):
    return render(request, 'destination.html')

def logo(request):
    return render(request, 'index.html')

def contact_us(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact_us = contactus(name=name, contact=contact, email=email, message=message)
        contact_us.save()
      
    return render(request, 'contact_us.html')

def service(request):
    return render(request, 'service.html')

def FAQs(request):
    return render(request, 'FAQs.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def tfare(request):
    return render(request, 'tfare.html')

def user(request):
    return render(request, 'user.html')

def userdetail(request):
    return render(request, 'userdetail.html')

def payment(request):
    return render(request, 'payment.html')

def userbooking(request):
    return render(request, 'userbooking.html')

def signUp(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        phnum=request.POST.get('phnum')
        emailid=request.POST.get('emailid')
        pswd=request.POST.get('pswd')
        sign= signup(fname=fname, lname=lname, phnum=phnum, emailid=emailid, pswd=pswd)
        sign.save()

    return render(request, 'signUp.html')
    

def tbooking(request):
    if request.method=="POST":
        pname=request.POST.get('pname')
        pemail=request.POST.get('pemail')
        pnum=request.POST.get('pnum')
        clocation=request.POST.get('clocation')
        destination=request.POST.get('destination')
        sdate=request.POST.get('sdate')
        adults=request.POST.get('adults')
        child=request.POST.get('child')
        book_ticket = bookticket(pname=pname, pemail=pemail, pnum=pnum, clocation=clocation, destination=destination, sdate=sdate, adults=adults, child=child)
        book_ticket.save()

    return render(request, 'tbooking.html')
