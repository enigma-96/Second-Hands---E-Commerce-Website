from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required

def home_view(request):
	return render(request,'Home.html')

def index_view(request):
	return render(request,'index.html')

def Beds_view(request):
	return render(request,'Beds.html')

def Sofas_view(request):
	return render(request,'Sofas.html')

def Tables_view(request):
	return render(request,'Tables.html')

def Aboutus_view(request):
	return render(request,'Aboutus.html')

def contact_view(request):
	return render(request,'contact.html')

def payment_view(request):
	return render(request,'payment.html')

def cart_view(request):
	return render(request,'cart.html')

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			# log the user in
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})



def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in user
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('index')
	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})


def logout_view(request):
	logout(request)
	return redirect("home")
