from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from django.shortcuts import redirect, render
from .models import Books, Profile , Store          
from .form import CustomUserCreationForm,BooksForm,StoreForm,StorebookForm
from  bookstore.settings import GOOGLE_API_KEY,BASE_URL
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
import json

# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist')
       
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else'home')
        else:
            messages.error (request,"username or password is incorrect") 
    
    return render(request, 'User/login.html')

def registeruser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account has created!')

            login (request,user)
            return redirect('home')
        
        else:
            messages.error(request,'An error has beeen occurred buring registration')

    context = {'form':form }
    return render(request,"User/register.html",context)

def logoutuser(request):
    logout(request)
    messages.info(request,"user was logged out")
    return redirect('login')

@login_required (login_url="login")
def home(request):
    profile = request.user.profile
    store = profile.store_set.all()
    context = {'profile':profile,'store':store}
    return render(request,"home.html",context)

@login_required (login_url="login")
def storeview(request,pk):
    store = Store.objects.get(Id=pk)
    book = store.Books.all()
    print (type(book))
    context = {'store':store,'book':book}
    return render(request,"storedetails/storeView.html",context)

@login_required (login_url="login")
def bookview(request,pk):
    book = Books.objects.get(Id=pk)
    context = {'book':book}
    return render(request,"bookfile/bookview.html",context)

@login_required (login_url="login")
def bookadd(request):
    form = BooksForm()

    if request.method == 'POST':
        form = BooksForm(request.POST,request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            a = form.cleaned_data['Book_name']
            google = requests.get(BASE_URL+a+GOOGLE_API_KEY).json()
            for item in google['items'] :
                data=item['volumeInfo']
                da = data['title']
                if da == a :
                    book.Book_id = item['id']
            form.save()
            print(book.Book_id)

            return redirect ('home')

    context = {'form':form,}
    return render(request,"bookfile/bookadd.html",context)

@login_required (login_url="login")
def bookedit(request,pk):
    book = Books.objects.get(Id=pk)
    form = BooksForm(instance=book)
    if request.method == 'POST':
        form = BooksForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,"bookfile/bookadd.html",context)

@login_required (login_url="login")
def bookdelete (request,pk):
    book = Books.objects.get(Id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    context = {'object':book}
    return render(request,'bookfile/bookdelete.html',context)

@login_required (login_url="login")
def storeadd(request):
    profile = request.user.profile
    form = StoreForm()

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = profile                
            form.save()
            return redirect ('home')

    context = {'form':form}
    return render(request,"storedetails/storeadd.html",context)

@login_required (login_url="login")
def storeedit(request,pk):
    store = Store.objects.get(Id=pk)
    form = StoreForm(instance=store)
    if request.method == 'POST':    
        form = StoreForm(request.POST,instance=store)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,"storedetails/storeadd.html",context)

@login_required (login_url="login")
def storedelete(request,pk):
    store = Store.objects.get(Id=pk)

    if request.method == 'POST':
        store.delete()
        return redirect('home')

    context = {'object':store}
    return render(request,'bookfile/bookdelete.html',context)

@login_required (login_url="login")
def storeeditadd(request,pk):
    store = Store.objects.get(Id=pk)
    form = StorebookForm(instance=store)
    
    if request.method == 'POST':    
        form = StoreForm(request.POST,instance=store)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,"storedetails/storeaddbook.html",context)