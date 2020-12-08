from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.forms import CarForm,UserForm,AppointmentForm
from carpool.models import Car,User,Appointment
from django.contrib import messages
from django.contrib.sessions.models import Session
import mysql.connector
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
import datetime
from django.core.mail import send_mail


# Create your views here.
def login(request) :
    if request.session.has_key('loggedin'):
        return render(request, "index.html")
    else:
        return render(request, "login.html")
def Signup(request) :
    return render(request, "Signup.html")
def bindex(request) : 
    if request.session.has_key('loggedin'):
       return render(request, "index.html")
    else:
        return render(request, "bindex.html")
def index(request) :
    if request.session.has_key('loggedin'):
       return render(request, "index.html")
    return redirect('login')

def about(request) :
    if request.session.has_key('loggedin'):
       return render(request, "about.html")
    return redirect('login')
def services(request) :
    if request.session.has_key('loggedin'):
        return render(request, "services.html")
    return redirect('login')
def team(request) :
    if request.session.has_key('loggedin'):
       return render(request, "team.html")
    return redirect('login')
def project(request) :
    if request.session.has_key('loggedin'):
        return render(request, "project.html")
    return redirect('login')
def blog(request) :
    if request.session.has_key('loggedin'):
        return render(request, "blog.html")
    return redirect('login')
def contact(request) :
    if request.session.has_key('loggedin'):
        return render(request, "contact.html")
    return redirect('login')
def comingsoon(request) :
    if request.session.has_key('loggedin'):
       return render(request, "comingsoon.html")
    return redirect('login')


def user(request) :
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
        msg1 = 'successfully registered'
        return render(request,"Signup.html", {'msg1':msg1})
    except:
        msg = 'Username or Car Alredy registered Helps check'
        return render(request,"Signup.html", {'msg':msg})
    
   
def logins(request) :
    
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
            request.session['loggedin'] = True
            return render(request, "index.html",{'user':username})

        else:
            msg = 'Incorrect username/password!'
            return render(request,"login.html", {'msg':msg})
        close.mycursor

def book(request) :
    service = request.POST["service"]
    name = request.POST["name"]
    regno =  request.POST["regno"]
    reg = regno.upper()
    msg = request.POST["message"]
    time = request.POST["time"]
    datee = request.POST["date"]
    d,m,y = datee.split("-")
    m1 = int(m)
    d1 = int(d)
    y1 = int(y)
    today = datetime.datetime.now()
    d = today.strftime("%m/%d/%y")
    mm,dd,yy = d.split("/")
    ddd = int(dd)
    mmm = int(mm)
    yyy = int(yy)
    if (m1 >= mmm) and (d1 >= ddd) and (y1 >= yyy):
        
            try:
                data = User.objects.filter(regno=reg).values('user_name','address', 'phone','cartype')
                if data:
                    for data in data:
                      un =data['user_name']
                      add = data['address']
                      ctype = data['cartype']
                      ph = data['phone']
                else:
                      msg1 = 'Please Enter a valid Register number'
                      return render(request,"index.html", {'msg1':msg1})
            except:
                msg1 = 'Please Enter a valid Register number'
                return render(request,"index.html", {'msg1':msg1})
            try:
                 book = Appointment(service=service,name=name,regno=reg,phone=ph,date=datee,time=time,msg=msg,address=add,cartype=ctype)
                 book.save()
                 msg1 = 'Appointment successfully'
                 return render(request,"index.html", {'msg1':msg1})
            except:
                 msg = 'Appointment Unsuccessfully '
                 return render(request,"index.html", {'msg':msg})
    else:
         msg = 'Invalid Date Selected '
         return render(request,"index.html", {'msg':msg})


def logout(request) :
    if request.session.has_key('loggedin'):
       request.session.flush()
    return render(request,"login.html")


