from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import Profile

def index(request):
    return render(request,'index.html')


def signup(request):


    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       if password == password2:
          if User.objects.filter(username=username).exists():
             messages.info(request,'Username is taken')
             return redirect('signup')
          elif User.objects.filter(email=email).exists():
             messages.info(request,'Email is taken')
             return redirect('signup')
          else:
             user = User.objects.create_user(username=username,email=email,password=password)
             user.save()
         
            #create user profile object for new user
             user_model = User.objects.get(username=username)
             new_profile = Profile.objects.create(user=user_model)
             new_profile.save()
             return redirect('signup')
            

       else:
          messages.info(request,'password does not match')
          return redirect('signup.html')
    
    else:

      return render(request,'signup.html')
    


def signin(request):
   return render(request,'signin.html')