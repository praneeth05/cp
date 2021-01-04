"""cp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carpool import views

urlpatterns = [
    path('', views.bindex, name='bindex'),
    path('bindex', views.bindex, name='bindex'),
    path('index', views.index, name='index'),
    path('bookings', views.bookings, name='bookings'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('comingsoon', views.comingsoon, name='comingsoon'),
    path('login', views.login, name='login'),
    path('Signup', views.Signup, name='Signup'),
    path('user', views.user, name='user'),
    path('logins', views.logins, name='logins'),
    path('logout', views.logout, name='logout'),
    path('book', views.book, name='book' ),
    path('packbook', views.packbook, name='packbook' ),
    path('profile', views.profile, name='profile' ),
    path('gallery', views.gallery, name='gallery' ),
    path('message', views.message, name='message' ),
    path('subscriptions', views.subscriptions, name='subscriptions' ),
    path('forgotpassword', views.forgotpassword, name='forgotpassword' ),
    path('forgetpass', views.forgetpass, name='forgetpass' ),
    path('edituser', views.edituser, name='edituser' ),
    path('updateuser', views.updateuser, name='updateuser' ),
    path('updatepass', views.updatepass, name='updatepass' ),
    path('Messages', views.Messages, name='Messages' ),
]
