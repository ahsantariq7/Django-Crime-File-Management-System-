from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from django.shortcuts import render, HttpResponse,redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
import system
from system.models import  AddMissingPerson,ShowMostWantedPerson,AddComplaint
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy 
from .models import AddComplaint, AddMissingPerson, Crime,FIR,Contact
from django.contrib import messages
from .forms import AddMissingPersonForm
from .forms import ShowMostWantedPersonForm

# Create your views here.
# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):

    return render(request, 'index.html')

def base(request):
    return render(request,'base.html')

def expression(request):
    
    return render(request, 'ticketbook.html')

@login_required
def service(request):
   
    return render(request, 'services.html')

def about(request):
   
    return render(request, 'about.html')




class AddMissingPerson(ListView):
    model = AddMissingPerson
    template_name = "showmissingperson.html"

class CreatePostView(CreateView):  # new
    model = AddMissingPerson
    form_class = AddMissingPersonForm
    template_name = "post.html"
    success_url = reverse_lazy("miss")

class ShowMostWantedPerson(ListView):
    model = ShowMostWantedPerson
    template_name = "showmostwantedperson.html"

class CreatePostView2(CreateView):  # new
    model = ShowMostWantedPerson
    form_class = ShowMostWantedPersonForm
    template_name = "post3.html"
    success_url = reverse_lazy("post2")
    

def firwrite(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        firwrite=FIR(name=name, email=email, phone=phone, reason=reason,date=datetime.today())
        firwrite.save()
        messages.success(request, 'A FIR Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'addfir.html') 



def crime1(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        crime = request.POST.get('crime')
        crime1=Crime(name=name, email=email, phone=phone,address=address, crime=crime,date=datetime.today())
        crime1.save()
        messages.success(request, 'A Crime Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'addcrime.html') 

def addcomplaint(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        complaint = request.POST.get('complaint')
        addcomplaint=AddComplaint(name=name, email=email, phone=phone,address=address, complaint=complaint,date=datetime.today())
        addcomplaint.save()
        messages.success(request, 'A Complaint Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'addcomplaints.html') 

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'A Contact Message Received.')
    #return HttpResponse("This is Service page")
    #return HttpResponse("This is Contact page")
    return render(request, 'contact.html') 