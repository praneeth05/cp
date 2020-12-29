from django.shortcuts import render, redirect
from django.http import HttpResponse
from carpool.forms import UserForm,AppointmentForm,CarpriceForm,PackageForm,MessageForm
from carpool.models import User,Carprice,Appointment,Package,Message
from django.contrib import messages
from django.contrib.sessions.models import Session
import mysql.connector
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from datetime import date 
import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.utils.html import strip_tags

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
def forgetpass(request) :
    return render(request, "forgetpass.html")
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
    try:
        su = request.session['username']
        suser = su.split('@')
        userinfo = User.objects.filter(user_name=su).values('user_name','address','cartype','regno','phone')
        for reg in userinfo:
            regn = reg['regno']
        userbook = Appointment.objects.filter(regno=regn).values('service','name','regno','date','time')
        count = len(userbook)
        
        return render(request, "userprofile.html", {'appointment':userbook,'info':userinfo,'user':suser[0],'tcount':count})
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')    
    
def bookings(request) :
    try:
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
        try:
            appointdata = Appointment.objects.values('service','name','regno','phone','date','time','msg','cartype')
            if appointdata:
                count = len(appointdata)
                return render(request, "bookings.html", {'appointment':appointdata,'user':suser[0],'tcount':count})
            else:
                mssg = "There is No Appointment to display"
                msg = "1"
                count = 0
                return render(request, "bookings.html", {'user':suser[0],'tcount':count,'mssg':mssg,'msg':msg})

        except:
            count = 0
            return render(request, "subscriptions.html", {'user':suser[0],'tcount':count})
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')

def subscriptions(request) :
    try:
        su = request.session['username']
        suser = su.split('@')
        #Pack = Package.objects.values('date','regno').all()   
        #for value in Pack:
           # regn = value['regno']
           # date3 = value['date']
           # d1 = datetime.datetime.strptime(date3, "%Y-%m-%d")
        today = date.today().isoformat()
        d2 = datetime.datetime.strptime(today, "%Y-%m-%d")
           # if d1 < d2:
               # todel = Package.objects.filter(date=date3)
               # todel.delete()
      
        packdata = Package.objects.values('service','name','regno','phone','date','time','msg','cartype','address')
        if packdata:
            count = len(packdata)
            return render(request, "subscriptions.html", {'package':packdata,'user':suser[0],'tcount':count,'date':d2})
        else:
            mssg = "There is No subscriptions to display"
            msg = "1"
            count = 0
            return render(request, "subscriptions.html", {'user':suser[0],'tcount':count,'mssg':mssg,'msg':msg})
        
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')

def gallery(request) :
    if request.session.has_key('username'):
        su = request.session['username']
        suser = su.split('@')
        return render(request, "gallery.html", {'user':suser[0]})
    return redirect('login')

def user(request) :
    try:
        user_name = request.POST["user_name"]
        name = user_name.split("@")
        password =  request.POST["password"]
        address = request.POST["address"]
        cartype = request.POST["cartype"]
        regno = request.POST["regno"]
        regno = regno.upper()
        mob = request.POST["phone"]
        try:
            users_info = User(user_name=user_name,password=password,address=address,cartype=cartype,regno=regno,phone=mob)
            users_info.save()
            try:
                html_content = render_to_string("C:/cp/carpool/templates/emailsingup.html",{'name':name[0],'username': user_name,'password':password,'cartype': cartype,'mob':mob,'address':address})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    "Sing Up Successfull !",
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [user_name]
                    )
                email.attach_alternative(html_content,"text/html")
                email.send()
            except:
                msg = 'appinternet'
                return render(request,"index.html", {'msg':msg, 'user':suser[0]})
            msg = 'success'
            return render(request,"Signup.html", {'msg':msg})
        except:
            msg = 'exits'
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
def forgotpassword(request):
    
    username = request.POST["username"]
    name = username.split("@")
    data = User.objects.filter(user_name=username).values('user_name','password')
    if data:
        for data in data:
            user_name = data['user_name']
            password = data['password']
        html_content = render_to_string("C:/cp/carpool/templates/emailforgetpass.html",{'name':name[0],'username': user_name,'password':password})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "CarPool Account Credentials",
            text_content,
            settings.EMAIL_HOST_USER,
            [user_name]
            )
        email.attach_alternative(html_content,"text/html")
        email.send()
        msg = '1'
        return render(request,"forgetpass.html", {'msg':msg,'email':user_name})
    else:
        msg = '2'
        return render(request,"forgetpass.html", {'msg':msg})
   
                
def book(request) :
    try:
        service = request.POST["service"]
        name = request.POST["name"]
        recp = name.upper()
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
                            ct = ctype.upper()
                            ph = data['phone']

                            
                        price = Carprice.objects.filter(car_type = ct).values('intextwash','compwash','intdet','extdet','silver','gold','washtime','dettime')
                        if price:
                            for price in price:
                                intextwash = price['intextwash']
                                compwash = price['compwash']
                                intdet = price['intdet']
                                extdet = price['extdet']
                                silver = price['silver']
                                gold = price['gold']
                                washtime = price['washtime']
                                dettime = price['dettime']
                                
                                    
                            if service == "INTERIOR + EXTERIOR WASH":
                                charge = intextwash
                            elif service == "COMPLETE SUPERIOR WASH":
                                charge = compwash
                            elif service == "REMOVING HARD WATER STAIN":
                                if ct == "COMPACT SUV" or ct == "SUV":
                                    charge = '300'
                                else:
                                    charge = '250'
                            elif service == "INTERIOR DETAILING":
                                charge = intdet
                            elif service == "EXTERIOR DETAILING":
                                charge = extdet
                            else:
                                charge = '0'

                    else:
                        msg = '0'
                        return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                except:
                    msg = '0'
                    return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                try:
                    book = Appointment(service=service,name=name,regno=reg,phone=ph,date=datee,time=time,msg=mesg,address=add,cartype=ctype,charges=charge,Washtime=washtime,dettime=dettime)
                    book.save()
                    maxid = Appointment.objects.filter(service=service,name=name,regno=reg,phone=ph,date=datee,time=time,msg=mesg,address=add,cartype=ctype,charges=charge).values('id')
                    if maxid:
                        for id in maxid:
                            maxid = id['id']

                    try:
                        html_content = render_to_string("C:/cp/carpool/templates/emailapp.html",{'name': name,'Regno': reg,'cartype': ctype,'time': time,'service': service,'date': datee,'mob':ph,'charge':charge,'recp':recp,'id':maxid,'address':add,'Washtime':washtime,'dettime':dettime})
                        text_content = strip_tags(html_content)
                        email = EmailMultiAlternatives(
                            "Appointment Booked !",
                            text_content,
                            settings.EMAIL_HOST_USER,
                            [un,"akashraj.jain22@gmail.com"]
                            )
                        email.attach_alternative(html_content,"text/html")
                        email.send()
                    except:
                        msg = 'appinternet'
                        return render(request,"index.html", {'msg':msg, 'user':suser[0]})
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
def packbook(request):
    try:
        package = request.POST["package"]
        name = request.POST["name"]
        recp = name.upper()
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
                            ct = ctype.upper()
                            ph = data['phone']

                            
                        price = Carprice.objects.filter(car_type = ct).values('silver','gold','washtime')
                        if price:
                            for price in price:
                                silver = price['silver']
                                gold = price['gold']
                                washtime = price['washtime']
                                                            
                                    
                            if package == "SLIVER PACKAGE":
                                charge = silver
                            elif service == "GOLD PACKAGE":
                                charge = gold
                            else:
                                charge = '0'

                    else:
                        msg = '0'
                        return render(request,"index.html", {'msg':msg, 'user':suser[0]})
               
                except:
                    msg = '0'
                    return render(request,"index.html", {'msg':msg, 'user':suser[0]})
                try:
                    packagebook = Package(service=package,name=name,regno=reg,phone=ph,date=datee,time=time,msg=mesg,address=add,cartype=ctype,charges=charge,Washtime=washtime)
                    packagebook.save()
                    maxid = Package.objects.filter(service=package,name=name,regno=reg,phone=ph,date=datee,time=time,msg=mesg,address=add,cartype=ctype,charges=charge).values('id')
                    if maxid:
                        for id in maxid:
                            maxid = id['id']
                    
                    html_content = render_to_string("C:/cp/carpool/templates/emailpack.html",{'name': name,'Regno': reg,'cartype': ctype,'time': time,'service': package,'date': datee,'mob':ph,'charge':charge,'recp':recp,'id':maxid,'address':add})
                    text_content = strip_tags(html_content)
                    email = EmailMultiAlternatives(
                        "Monthly subscription Booked !",
                        text_content,
                        settings.EMAIL_HOST_USER,
                        [un]
                        )
                    email.attach_alternative(html_content,"text/html")
                    email.send()
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


def message(request):
    try:
        emailid = request.POST["email"]
        name = request.POST["name"]
        subject = request.POST["subject"]
        message =  request.POST["message"]
        mesg = Message(email_id=emailid,name=name,subject=subject,message=message)
        mesg.save()
        msg="sent"
        su = request.session['username']
        suser = su.split('@')
        return render(request,"contact.html", {'msg':msg, 'user':suser[0]})

    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')

def edituser(request):
    try:
        su = request.session['username']
        suser = su.split('@')
        userinfo = User.objects.filter(user_name=su).values('user_id','user_name','address','cartype','regno','phone')     
        return render(request, "userprofileedit.html", {'info':userinfo,'user':suser[0]})
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')  
def updateuser(request):
    try:
        su = request.session['username']
        suser = su.split('@')
        user_id = request.POST["user_id"]
        user_name = request.POST["user_name"]
        name = user_name.split("@")
        address = request.POST["address"]
        cartype = request.POST["cartype"]
        regno = request.POST["regno"]
        regno = regno.upper()
        mob = request.POST["phone"]
        password = User.objects.filter(user_id=user_id).values('password')
        for value in password:
            password = value['password']
        User.objects.filter(user_id=user_id).update(user_name=user_name,address=address,cartype=cartype,regno=regno,phone=mob)
        try:
            html_content = render_to_string("C:/cp/carpool/templates/emailupdate.html",{'name':name[0],'username': user_name,'password':password,'cartype': cartype,'mob':mob,'address':address})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Update Successfull !",
                text_content,
                settings.EMAIL_HOST_USER,
                [user_name]
                )
            email.attach_alternative(html_content,"text/html")
            email.send()
        except:
            msg = 'appinternet'
            return render(request,"index.html", {'msg':msg, 'user':suser[0]})
        request.session.flush()
        return render(request,"login.html")
    except:
        if request.session.has_key('username'):
            su = request.session['username']
            suser = su.split('@')
            return render(request, "index.html", {'user':suser[0]})
        return redirect('login')
def updatepass(request):
    try:
        su = request.session['username']
        suser = su.split('@')
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["password"]
        if oldpassword == newpassword:
            msg="sameasold"
            su = request.session['username']
            suser = su.split('@')
            userinfo = User.objects.filter(user_name=su).values('user_id','user_name','address','cartype','regno','phone')     
            return render(request, "userprofileedit.html", {'info':userinfo,'user':suser[0],'msg':msg})
        else:
            info = User.objects.filter(user_name=su).values('user_id','user_name','address','cartype','password')
            for value in info:
                user_id = value['user_id']
                password = value['password']
                user_name = value['user_name']
                address = value['address']
                cartype =value['cartype']
            if oldpassword == password:
                User.objects.filter(user_id=user_id).update(password=newpassword)
            
                html_content = render_to_string("C:/cp/carpool/templates/emailupdate.html",{'name':suser[0],'username': user_name,'password':newpassword,'cartype': cartype,'address':address})
                text_content = strip_tags(html_content)
                email = EmailMultiAlternatives(
                    "Password Successfull Updated !",
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [user_name]
                    )
                email.attach_alternative(html_content,"text/html")
                email.send()
                request.session.flush()
                return render(request,"login.html")
            else:
                msg="notsame"
                su = request.session['username']
                suser = su.split('@')
                userinfo = User.objects.filter(user_name=su).values('user_id','user_name','address','cartype','regno','phone')     
                return render(request, "userprofileedit.html", {'info':userinfo,'user':suser[0],'msg':msg})

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



