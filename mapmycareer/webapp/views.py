# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import webinar

def index(request):
 return render(request, 'webapp/index1.html')
 

def saveuserdata(request):
    if request.method == "POST":
       name = request.POST.get("name")
       email = request.POST.get("email")
       phoneno = request.POST.get("phone")
       city = request.POST.get("city")
       profession = request.POST.get("profession")
       wb = webinar(name=name, email=email, phone=phoneno, city=city, profession=profession)
       wb.save()
       return render(request, "webapp/thankyou.html")

def index10(request):
    return render(request, "webapp/index10.html")



