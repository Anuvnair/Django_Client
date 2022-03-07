from http import client
from pyexpat.errors import messages
from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.test import Client
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# function to render the home page
def frontend(request):
    return render(request,"frontend.html")

# function to render the backend page
@login_required(login_url="login")
def backend(request):
   if 'q' in request.GET:
       q=request.GET('q')
       all_client_list =Client.objects.filter(
           Q(name_icontains=q) | Q(phone=q) |Q(email=q) |Q(age=q) |Q(gender=q) |Q(note=q) 
       ).order_by('-created_at')
   else:
        all_client_list = Client.objects.all().oder_by('-created_at')

   Paginator = Paginator(all_client_list,4)
   page =request.GET.get('page')
   all_client =Paginator.get_page(page)

   return render(request,'backend.html',{"clients":all_client})

# function to insert patient
@login_required(login_url="login")
def add_patient(request):
   if request.method =="POST":
       if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('note'):
           client =Client()
           client.name = request.POST.get('name')
           client.phone = request.POST.get('phone')
           client.email = request.POST.get('email')
           client.age = request.POST.get('age')
           client.gender = request.POST.get('gender')
           client.note = request.POST.get('note')
           client.save()
           messages.success(request,"Client added successfully !")
           return HttpResponseRedirect('/backend')
   else:
        return render(request,"add.html")       