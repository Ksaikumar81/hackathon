from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path("about", views.about, name='about'),
    path("customers", views.customers, name='customers'),
    path("payment", views.payment, name='payment'),
    path("trans", views.trans, name='trans'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path('login1/',views.login1,name='login1'),
]