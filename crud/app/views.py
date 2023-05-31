from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def signup(request):
    return render(request,'signup.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = make_password(request.POST['password'])
        if Person.objects.filter(email=email).exists():
            messages.error(request,'Email already exist')
            return redirect('/')
        else:
            Person.objects.create(name=name, email=email, mobile=mobile, password=password)
            return redirect('/login/')
        
def login(request):
    return render(request,'login.html')

# def login_request(request):
#     if request.method=='POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=email, password= password)
#         print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",user)
#         if user is not None:
#                 auth.login(request,user)
#                 messages.success(request,'Welcome')
#                 return render(request,'index.html')

#         else:
#             messages.error(request,'Invalid Username and Password')
#             return redirect('/login/')
#     else:
#         return redirect('/login/')
    
def login_request(request):
    if request.method =='POST':
        email= request.POST['email']
        password = request.POST['password']
        if Person.objects.filter(email = email).exists():
            obj= Person.objects.get(email=email)
            if check_password(password,obj.password):
               messages.success(request,'Welcome')
               return redirect('/table/')
            else:
                messages.error(request,'Invalid Username and Password')
                return redirect('/login/')
    else:
        # messages.error(request,'Invalid Username and Password')
        return redirect('/login/')
    
def data(request):
    user_data=Person.objects.all()
    return render(request, 'index.html',{'user_data':user_data})

def deleteuser(request):
    id = request.GET['id']
    Person.objects.get(id=id).delete()
    user_data=Person.objects.all()
    return render(request, 'index.html',{'user_data':user_data})

def searchdata(request):
    id= request.GET['id']
    user_data=Person.objects.filter(id=id).all()
    print('XXXXXXXXXXXXXXXXXXxxx',user_data)   
    return render(request, 'index.html',{'user_data':user_data})
   
def show_all_data(request):
    user_data=Person.objects.all()
    return render(request, 'index.html',{'user_data':user_data})

def updateuser(request):
    p= Person()
    ids=request.POST['id']
    if ids is not '':
        p.id =ids
    p.name = request.POST['name']
    p.email= request.POST['email']
    p.mobile = request.POST['mobile']
    p.save()
    user_data=Person.objects.all()
    return render(request,'index.html',{'user_data':user_data})
        

    
    