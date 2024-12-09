from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Profile
from django.views.generic import View


import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):
    
    logger.info(f"User authenticated: {request.user.is_authenticated}")
    print(request.user)
    return render(request, 'index.html')


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
             user_login = authenticate(username=username, password=password)
             login(request, user_login)
            
         
            #create user profile object for new user
             user_model = User.objects.get(username=username)
             new_profile = Profile.objects.create(user=user_model)
             new_profile.save()
             return redirect('settings')
            

       else:
          messages.info(request,'password does not match')
          return redirect('signup')
    
    else:

      return render(request,'signup.html')
    

class SigninView(View):

   template_name = "signin.html"

   def get(self,request):
      return render(request,"signin.html")
   

   def post(self,request):
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)
      if user :
         login(request, user)
         return redirect('/')
      else:
          messages.error(request,'Invalid credential')
      
      return render(request, self.template_name)


class LogoutView(LoginRequiredMixin, View):
    login_url = 'signin'  # Redirects unauthenticated users to signin

    def get(self, request):
        logout(request)
        print("User logged out")
        return redirect('signin')
   

# class SettingView(LoginRequiredMixin,View):
#    login_url = 'signin'
   
#    def get(self,request):
#       user_profile = Profile.objects.get(user=request.user)
#       return render(request,'setting.html',{'user_profile':user_profile})
   
#    def post(self, request):
#        user_profile = Profile.objects.get(user=request.user)
       
#        if request.FILES.get('image') == None:
#           image = user_profile.profileimg
#           bio = request.POST['bio']
#           location = request.POST['location']

#           user_profile.profileimg = image
#           user_profile.bio = bio
#           user_profile.location = location
      
#        if request.FILES.get('image') != None:
#           image = user_profile.profileimg
#           bio = request.POST['bio']
#           location = request.POST['location']

#           user_profile.profileimg = image
#           user_profile.bio = bio
#           user_profile.location = location
#           user_profile.save()
          

       
#        return redirect('settings')



class SettingView(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request):
        user_profile = Profile.objects.get(user=request.user)
        return render(request, 'setting.html', {'user_profile': user_profile})

    def post(self, request):
        user_profile = Profile.objects.get(user=request.user)
        bio = request.POST.get('bio')
        location = request.POST.get('location')

        # Check if a new image is uploaded
        if request.FILES.get('image'):
            user_profile.profileimg = request.FILES['image']  # Assign the uploaded image
        
        # Update other profile fields
        user_profile.bio = bio
        user_profile.location = location

        # Save the profile
        user_profile.save()
        return redirect('settings')


@login_required
def UploadPost(request):
   pass