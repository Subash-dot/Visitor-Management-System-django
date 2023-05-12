from django.utils import timezone
from datetime import *
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from .models import Visitor, ExcelFile
from .forms import VisitorForm
import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def base(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def visitor_create_view(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor')
    else:
        form = VisitorForm()
    return render(request, 'visitoradd.html', {'form': form})

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())


@login_required
def visitor(request):
    visitors = Visitor.objects.all().values()
    template = loader.get_template('visitor.html')
    context = {
        'visitors' : visitors,
    }
    return HttpResponse(template.render(context, request))

@login_required
def checkout(request, pk):
    visitor = Visitor.objects.get(id=pk)
    current_time = datetime.now(timezone.utc)
    visitor.check_out = current_time
    visitor.save()
    return redirect('visitor')


@login_required
def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['files']
        visitor_data = ExcelFile.objects.create(
            file = file
        )
        path = str(visitor_data.file)
        print(f'{settings.BASE_DIR} + {path}')
        excel_read = pd.read_excel(path)
        for data in excel_read.values:
            Visitor.objects.create(
                first_name=data[0],
                last_name=data[1],
                email=data[2],
                phone=data[3],
                address=data[4],
                company=data[5],
                purpose=data[6],
                check_in=data[7],
                check_out=data[8],
                host=data[9]
            )     
    return render(request, 'import.html')


@login_required
def qr(request):
    temp = loader.get_template('qr.html')
    return HttpResponse(temp.render())

@login_required
def details(request,id):
    visitor = Visitor.objects.get(id=id)
    temp = loader.get_template('details.html')
    context = {
        'visitor':visitor,
    }

    return HttpResponse(temp.render(context,request))

@login_required
def update(request, id):
    visitor = Visitor.objects.get(id=id)
    next= request.GET.get('next')

    context={
        'visitor':visitor
    }
    
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        company = request.POST.get('company')
        purpose = request.POST.get('purpose')
        host = request.POST.get('host')

        visitor.first_name = first_name
        visitor.last_name = last_name
        visitor.email = email
        visitor.phone = phone
        visitor.address = address
        visitor.company = company
        visitor.purpose = purpose
        visitor.host = host
        visitor.save()


        if next:
            return redirect(f'{next}')
        else:
            return redirect('/visitor')
    
    return render(request, 'update.html', context)



@login_required
def delete(request,id):
    visitor = Visitor.objects.get(id=id)
    visitor.delete()

    return redirect('/visitor')


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            next = request.GET.get('next')
            
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next:
                    return redirect(f'{next}')
                else:
                    return HttpResponseRedirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')
        return render(request, 'user/login.html')




def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if username and email and password:
                if password == password2:
                    user = User.objects.create(
                        email=email,
                        username=username,
                        password=password,
                    )
                    user.save()
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "The two password fields didn'/t match.")
                    return HttpResponseRedirect('/register')
            else:
                messages.error(request, "All fields are required.")
                return HttpResponseRedirect('/register')
        
    return render(request,'user/register.html')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")

    return redirect("/login")