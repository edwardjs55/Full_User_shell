from __future__ import unicode_literals
# from django.http import HttpResponse
import time
from datetime import datetime
from django.utils import timezone
import bcrypt
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse, redirect, render
from .models import User  #,Appt

now = (datetime.now().strftime('%Y-%m-%d'))

def init(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = -1  
        # print('(init): initial session_id: ',request.session['user_id'])          

def home(request):
    return render(request, "registration/home.html")

def registered(request):
    return render(request, "registration/registered.html")

def gotologin(request):
    return render(request, "registration/login.html")

def loggedin(request):
    return render(request, "registration/loggedin.html")

def loggedout(request):
    return render(request, "registration/loggedout.html")

def user(request):
    # if request.method == 'POST':
    #     post_data = {
    #             "name": request.POST['name'],
    #             "alias": request.POST['alias'],
    #             "email": request.POST['email'],
    #             "birthdate": request.POST['birthdate'],
    #             "user_id": request.session['user_id'],               
    #         }
    #     result = User.objects.update_validator(post_data)
    #     print( result)
    #     print('result[0]=', result[0])
    #     if result[0]:
    #         return redirect("registration/index.html")
    #     else:
    #         for item in result[1].values():
    #             messages.error(request, item)            
    #         return redirect("/user")
        
    # else:    
    init(request)
    if request.session['user_id'] == -1 :
        return render(request, 'registration/login.html')
    user = User.objects.get(id=request.session['user_id'])

    context = { 'user' : user,
                'bday' : user.birthdate.strftime("%Y-%m-%d")}
    return render(request,'registration/user.html',context)

def update(request):
    if request.method == 'POST':
        post_data = {
                "name": request.POST['name'],
                "alias": request.POST['alias'],
                "email": request.POST['email'],
                "birthdate": request.POST['birthdate'],
                "user_id": request.session['user_id'],               
            }
        result = User.objects.update_validator(post_data)
        print( result)
        print('result= ', result)
        if result[0]:
            return redirect("user")
        else:
            for item in result[1].values():
                messages.error(request, item)            
            return redirect("user")

def index(request):
    init(request)    
    return render(request,'registration/index.html')

def register(request):
    if request.method == 'POST':
        post_data = {
                "name": request.POST['name'],
                "alias": request.POST['alias'],
                "email": request.POST['email'],
                "birthdate": request.POST['birthdate'],
                "password": request.POST['password'],
                "confirm": request.POST['confirm'],
            }
        result = User.objects.register_validator(post_data)
        print( result)
        print('result[0]=', result[0])
        if result[0]: #success
            request.session['user_id'] = result[1] # result[1].id
            return redirect("user")
            #return redirect("/loggedin")
        else:        #failed
            # print '[1]', result[1], result[1]['user_name']
            for item in result[1].values():
                messages.error(request, item)
            
            return redirect("index")      
        #request.session['user_id'] = User.objects.get(user_name = user)
        #return redirect('/blogs')
        #return render(request,'travelbuddy/travels.html')

def login(request):
    if request.method == 'POST':
        post_data = {
                "email": request.POST['email'],
                "password": request.POST['password'],                
            }            
        result = User.objects.login_validator(post_data)
       
        if result[0]: #success
            # print result
            request.session['user_id'] = result[1]
            print('session_id: ', request.session['user_id'])
            return redirect("loggedin")
        else:
            #print('[1]', result[1], result[1]['user_name'])
            print("login Error")
            for item in result[1].values():
                messages.error(request, item)            
            return render(request,"registration/login.html") #redirect("/")
        
def logout(request): # delete user cookie N goto root page
    request.session.flush()   # clear()
    return redirect('loggedout')

def updateUser(request):
    return redirect("/")





