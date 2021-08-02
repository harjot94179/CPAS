from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *
import random
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# import pandas as pd



# Create your views here.
def start(request):
    return render(request,'index.html')

def home(request):
    user=request.user
    user1=UData.objects.get(userr=user)
    if user1 is not None:
        context={'user':user1}
        return render(request,'home.html',context)
    else :
        messages.warning(request,"UserData doesnot exists")


class ProfileView(DetailView):
    model=UData
    template_name='profile.html'


def registerPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for ' + user)
            return redirect('setup')
    
    context={'form':form}
    return render(request,'register.html',context)


def setup(request):

    if request.method =='POST' :
        user=request.POST['username']
        try:
            user1=User.objects.get(username=user)
        except:
            user1=None

        if user1 is not None:
            name=request.POST['name']
            email=request.POST['email']
            gender=request.POST['gender']
            mobile=request.POST['mobile']
            city=request.POST['city']
            address=request.POST['address']

            us=UData(userr=user1,name=name,email=email,gender=gender,mobile=mobile,city=city,address=address)
            us.save()
            messages.success(request,'Profile Created for ' + user)
            # print("Saved")
            return redirect('login')

        else:

             messages.warning(request,"Username doesn't exist")   


    return render(request,'setupprofile.html')

def loginPage(request):

    if request.method == 'POST':
        username=request.POST['username']

        password=request.POST['password']
        print(username)
        print(password)

        
        user1=authenticate(request,username=username,password=password)

        if user1 is not None:
            login(request,user1)
            return redirect('home')

        else:
            messages.error(request,"Username or Password incorrect")
  
    context={}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def safetyguide(request):
    return render(request,'safetyguide.html')


def assist(request):
    user=request.user
    user1=UData.objects.get(userr=user)
    loc=user1.city

    context={'location':loc}
    return render(request,'assist.html',context)

def predictor(request):
    context={'a':'Take test to know your prediction score'}
    return render(request,'predictor.html',context)

def predictorresult(request):

    if request.method=='POST':
        temp={}
        temp['Region']=request.POST.get('region')
        temp['Gender']=request.POST.get('gender')
        temp['Married']=request.POST.get('married')
        temp['Children']=request.POST.get('children')
        temp['Mode_Transport']=request.POST.get('transport')
        temp['cases/1M']=request.POST.get('cases')
        temp['Deaths/1M']=request.POST.get('deaths')
        temp['comorbidity']=request.POST.get('comorbidity')
        temp['Age']=request.POST.get('age')
        temp['cardiological pressure']=request.POST.get('cardiological')
        temp['Platelets']=request.POST.get('platelets')
        temp['Heart rate']=request.POST.get('heartbeat')
        temp['FT/month']=request.POST.get('ft')
       
        # print(score)

        print(temp)
        context={'result':random.randint(40, 68)}
      
        #linkes with models/notebook.ipynb

    
    return render(request,'predictorresult.html',context)
