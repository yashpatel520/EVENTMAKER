from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Profile


def LoginPageView(request):
	if request.user.is_authenticated:
		messages.success(request,' You are already login ')
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				if user.is_staff:
					login(request, user)
					return redirect('eventportal')
				else:
					login(request, user)
					return redirect('home')
			else:
				messages.info(request, 'username  OR password is incorrect')

		return render(request, 'accounts/login.html')

def RegisterPageView(request):
	if request.method == 'POST':
		username = request.POST['username']
		fname = request.POST['fname']
		mname = request.POST['mname']
		lname = request.POST['lname']
		mobile = request.POST['tel']
		email = request.POST['email']
		password = request.POST['Password']
		cpassword = request.POST['cPassword']
		if password == cpassword:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'User Name is already taken')
				return redirect("register")
			elif User.objects.filter(email=email).exists():
				messages.error(request, 'Email Adress is already taken')
				return redirect("register")
			elif Profile.objects.filter(mobile=mobile).exists():
				messages.error(request, 'Mobile Number is already taken')
				return redirect("register")
			else:
				users = User.objects.create_user(username=username,first_name=fname, last_name=lname, email=email,password=password)
				users.save()
				profile = Profile.objects.get(user = users.id)
				profile.usertype = 'customer'
				profile.mobile = mobile
				profile.middle_name = mname
				profile.save()
				messages.success(request,'Account Created! Please Login Here !!')
				return redirect("login")
		messages.error(request, 'Password And Confrim Password are not matching')
		return redirect("register")	
	return render(request, 'accounts/register.html')


def logoutUser(request):
	logout(request)
	return redirect('login')

