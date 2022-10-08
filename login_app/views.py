from django.shortcuts import render, redirect
from login_app.models import *
from django.contrib import messages
import bcrypt

def index(request):
    # if 'user_id' in request.session:
    #     return redirect('/success/')
    # del request.session['user_id']
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['psw']
        psw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(psw_hash)
        new_user=User.objects.create(firstname=request.POST['fname'], 
        lastname=request.POST['lname'], email=request.POST['email'], password=psw_hash)
        request.session['user_id']=new_user.id

    return redirect('/success/')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['psw-login'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/success/')
    
    return redirect('/')

def success(request):
    if 'user_id' in request.session:
        # context={
        #     'user':User.objects.get(id=request.session['user_id'])
        # }
        return redirect('/dashboard/')
    else:
        return redirect('/')

def logout(request):
    del request.session['user_id']

    return redirect('/')