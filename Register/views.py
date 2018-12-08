from django.shortcuts import render

# Create your views here.
from django.template import  loader
from django.http import HttpResponse
import Register
from Register.forms import RegisterForm
from .forms import RegisterForm
from django.shortcuts import render
from User.models import User

def index(request):

    if request.method == 'POST':
        data = RegisterForm(request.POST)
        if data.is_valid():
            dummy = User()
            dummy.email = data.cleaned_data['email']
            dummy.password = "dummy-pass"
            dummy.username = data.cleaned_data['name']
            dummy.save()

    form = RegisterForm()
    return render(request,'Register/index.html',{'form' : form})

def display(request):
    all = User.objects.all()
    return render(request,'Register/display.html',{'users':all})