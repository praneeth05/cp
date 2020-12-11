from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.forms import UserForm,AppointmentForm,HatchbackForm,SedanForm,CompactsuvForm,SuvForm
from carpool.models import User,Hatchback,Sedan,Compactsuv,Suv,Appointment
from django.contrib import messages
from django.contrib.sessions.models import Session
import mysql.connector
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from datetime import date 
import datetime
from django.core.mail import send_mail


# Create your views here.
def login(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "index.html", {'user':suser[0]})
    else:
        return render(request, "login.html")
def Signup(request) :
    return render(request, "Signup.html")
def bindex(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@') 
        return render(request, "index.html", {'user':suser[0]})
    else:
        return render(request, "bindex.html")
def index(request) :
    if request.session.has_key('username'):
       su = request.session['username']
       suser = su.split('@')
       return render(request, "index.html", {'user':suser[0]})
    return redirect('login')

def about(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "about.html", {'user':suser[0]})
    return redirect('login')
def services(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "services.html", {'user':suser[0]})
    return redirect('login')
def team(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "team.html", {'user':suser[0]})
    return redirect('login')
def project(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "project.html", {'user':suser[0]})
    return redirect('login')
def blog(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "blog.html", {'user':suser[0]})
    return redirect('login')
def contact(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "contact.html", {'user':suser[0]})
    return redirect('login')
def comingsoon(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "comingsoon.html", {'user':suser[0]})
    return redirect('login')
def profile(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "userprofile.html", {'user':suser[0]})
    return redirect('login')


def user(request) :
    try:
        user_name = request.POST["user_name"]
        password =  request.POST["password"]
        address = request.POST["address"]
        cartype = request.POST["cartype"]
        regno = request.POST["regno"]
        regno = regno.upper()
        mob = request.POST["phone"]
        try:
            users_info = User(user_name=user_name,password=password,address=address,cartype=cartype,regno=regno,phone=mob)
            users_info.save()
            msg = '1'
            return render(request,"Signup.html", {'msg':msg})
        except:
            msg = '0'
            return render(request,"Signup.html", {'msg':msg})
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')
       
def logins(request) :
    try:
        username = request.POST["username"]
        password =  request.POST["password"]
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="carpool"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM users WHERE user_name = %s AND password = %s", (username, password,))
        account = mycursor.fetchone()

        if account:
            request.session['username'] = username
            su = request.session['username']
            suser = su.split('@')
            
            booked = Appointment.objects.values('date','regno').all()
          
            for value in booked:
                regn = value['regno']
                date3 = value['date']
                d1 = datetime.datetime.strptime(date3, "%Y-%m-%d")
                today = date.today().isoformat()
                d2 = datetime.datetime.strptime(today, "%Y-%m-%d")
                if d1 < d2:
                    todel = Appointment.objects.filter(date=date3)
                    todel.delete()
               
            msg ='4'
            return render(request,"index.html", {'msg':msg, 'user':suser[0]})                    
            
        else:
            msg = '0'
            return render(request,"login.html", {'msg':msg})
        close.mycursor
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')
                
def book(request) :
    try:
        service = request.POST["service"]
        name = request.POST["name"]
        regno =  request.POST["regno"]
        reg = regno.upper()
        mesg = request.POST["message"]
        time = request.POST["time"]
        datee = request.POST["date"]
        d1 = datetime.datetime.strptime(datee, "%Y-%m-%d")
        today1 = date.today().isoformat()
        d2 = datetime.datetime.strptime(today1, "%Y-%m-%d")
        su = request.session['username']
        suser = su.split('@')
        if d1 >= d2:
            
                try:
                    data = User.objects.filter(regno=reg).values('user_name','address', 'phone','cartype')
                    if data:
                        for data in data:
                            un =data['user_name']
                            add = data['address']
                            ctype = data['cartype']
                            ph = data['phone']
                    else:
                        msg = '0'
                        return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                except:
                    msg = '0'
                    return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                try:
                    book = Appointment(service=service,name=name,regno=reg,phone=ph,date=datee,time=time,msg=mesg,address=add,cartype=ctype)
                    book.save()
                    msg = '1'
                    return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                except:
                    msg = '2'
                    return render(request,"index.html", {'msg':msg, 'user':suser[0]})
        else:
            msg = '3'
            return render(request,"index.html", {'msg':msg, 'user':suser[0]})
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')


def logout(request) :
    if request.session.has_key('username'):
       request.session.flush()
    return render(request,"login.html")


