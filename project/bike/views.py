from django.shortcuts import render

from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model,login, authenticate
from django.contrib import auth
from django import forms
from django.views import generic
from .forms import ComplainForm
from .models import Complain
    
from django.urls import reverse_lazy
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from bike.models import *
import datetime
from random import *

def home(request):
    return render(request,'home.html')

def rent(request):
    Nbikes = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Normal').count()
    Cbikes = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Couple').count()
    Kbikes = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Kid').count()

    context = {
        'Couple':Cbikes,
        'Normal':Nbikes,
        'Kid':Kbikes,
    }

    return render(request,'rent.html',context)

def rentbike(request):
    if request.method=="POST":
        CNum = int(request.POST.get('CNum'))
        NNum = int(request.POST.get('NNum'))
        KNum = int(request.POST.get('KNum'))
        Usr = User.objects.create()
        Usr.save()
        
        time = datetime.datetime.now()
        Normal = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Normal')   
        Couple = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Couple')
        Kid = Bike.objects.filter(isBorrowed=False,isBroken=False,_type='Kid')
        cnt=0
        

        if(CNum != 0):
            for i in Couple:
                if(cnt==CNum):
                    cnt=0
                    break
                i.user = Usr
                i.startTime = time
                i.isBorrowed = True
                i.password=str(randint(1, 9999)).zfill(4)
                cnt+=1
                i.save()
                
        if(NNum != 0):
            for i in Normal:
                if(cnt==NNum):
                    cnt=0
                    break
                i.user = Usr
                i.startTime = time
                i.isBorrowed = True
                i.password=str(randint(1, 9999)).zfill(4)
                cnt+=1
                i.save()
                
        if(KNum != 0):
            for i in Kid:
                if(cnt==KNum):
                    cnt=0
                    break 
                i.user = Usr
                i.startTime = time
                i.isBorrowed = True
                i.password=str(randint(1, 9999)).zfill(4)
                cnt+=1
                i.save()
        
        BBike = Bike.objects.filter(user = Usr)

        context={
            '커플자전거':CNum,
            '일반자전거':NNum,
            '어린이자전거':KNum,
            'BBike':BBike,
            "User":Usr,
        }
    return render(request,'rentbike.html',context)

def claim(request):
    if request.method=="POST":
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/request/requestsuccess')
    else:
        form=ComplainForm()
    return render(request,'request.html',{'form':form})
