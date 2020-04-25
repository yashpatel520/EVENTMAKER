from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from .models import FeedBack,EventRegistration
from accounts.models import Profile
import datetime

def HomePageView(request):
	total_event =  EventRegistration.objects.all().count()
	total_customers = User.objects.filter(Q(is_superuser = 'False') & Q(is_staff = 'False')).count()
	total_comments = FeedBack.objects.all().count()
	total_events_done = EventRegistration.objects.filter(confirmation = 'completed').count()
	if request.user.is_authenticated:
		user= request.user
		posts = {'reviews': FeedBack.objects.all(),'events':EventRegistration.objects.filter(user_id=user),'total_event':total_event,'total_customers':total_customers,'total_comments':total_comments,'total_events_done':total_events_done,}
	else:
		posts = {'reviews': FeedBack.objects.all(),'total_event':total_event,'total_customers':total_customers,'total_comments':total_comments,'total_events_done':total_events_done,}
	return 	render(request, 'events/index.html', posts)

def EventPageView(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			Event_tpye = request.POST['eventType']
			Budget = request.POST['budget']
			if 'soundsystem' in request.POST:
				Soundsystem = request.POST['soundsystem']
			else:
				Soundsystem = 'not_enroll'
			if 'catering' in request.POST:
				Catering = request.POST['catering']
			else:
				Catering = 'not_enroll'
			if 'projector' in request.POST:
				Projector = request.POST['projector']
			else:
				Projector = 'not_enroll'
			if 'decoration' in request.POST:
				Decoration = request.POST['decoration']
			else:
				Decoration = 'not_enroll'
			if 'photographer' in request.POST:
				Photographer = request.POST['photographer']
			else:
				Photographer = 'not_enroll'
			Location = request.POST['Location']
			State = request.POST['State']
			Eventdate = request.POST['eventdate']
			City = request.POST['City']
			Comment = request.POST['Comments']
			Confirmation = 'pending'
			profile = Profile.objects.get(user=request.user)
			event_booking_request = EventRegistration.objects.create(location=Location,city=City,state=State,event_date=Eventdate,budget=Budget,event_type=Event_tpye,Sound_system=Soundsystem,Catering=Catering,Projector=Projector,Decoration=Decoration,Photographer=Photographer,confirmation=Confirmation,comment=Comment)
			event_booking_request.save()
			event = EventRegistration.objects.get(id=event_booking_request.id)
			event.user_id = request.user
			event.profile_id = profile
			event.save()
			messages.success(request, 'Success ! Your event has been booked..  ')
			return redirect('/')
		else:
			return render(request, 'events/events.html')
	
	else:
		messages.success(request,' Please Login First ')
		return redirect('login')


def EventPortalView(request):
	if request.user.is_authenticated:
		posts = {'events':EventRegistration.objects.all()}
		return render(request, 'events/event-portal.html',posts)
	else:
		messages.success(request,' Please Login First ')
		return redirect('login')

def ManagerEventViewForm(request, pk=None):

	if request.method == 'POST':
			if request.POST['action'] == 'accept':
				form =  EventRegistration.objects.get(id=pk)
				eventdate = form.event_date 
				if EventRegistration.objects.filter(Q(event_date=eventdate) & Q(confirmation='accepted')).exists():
					messages.error(request, 'You have already event on this date sorry')
					return redirect("eventportal")
				profile = Profile.objects.get(user=request.user)
				form.manager = request.user
				form.manager_profile_id = profile
				form.confirmation = 'accepted'
				form.confirmation_date = datetime.date.today() 
				form.save()
				return redirect('eventportal')
			elif request.POST['action'] == 'reject':
				form =  EventRegistration.objects.get(id=pk)
				profile = Profile.objects.get(user=request.user)
				form.manager = request.user
				form.manager_profile_id = profile
				form.confirmation = 'reject' 
				form.save()
				return redirect('eventportal')
			elif request.POST['action'] == 'update':
				form =  EventRegistration.objects.get(id=pk)
				if 'soundsystem' in request.POST:
					form.Sound_system = request.POST['soundsystem']
				else:
					form.Sound_system = 'not_enroll'
				if 'catering' in request.POST:
					form.Catering = request.POST['catering']
				else:
					form.Catering = 'not_enroll'
				if 'projector' in request.POST:
					form.Projector = request.POST['projector']
				else:
					form.Projector = 'not_enroll'
				if 'decoration' in request.POST:
					form.Decoration = request.POST['decoration']
				else:
					form.Decoration = 'not_enroll'
				if 'photographer' in request.POST:
					form.Photographer = request.POST['photographer']
				else:
					form.Photographer = 'not_enroll'
				form.save()
				return redirect('event_working_on')
			elif request.POST['action'] == 'done':
				form =  EventRegistration.objects.get(id=pk)
				form.confirmation = 'completed'
				form.save()
				return redirect('event_working_on')
			elif request.POST['action'] == 'Sound_system':
				form =  EventRegistration.objects.get(id=pk)
				form.Sound_system = 'not_enroll'
				form.save()
				return redirect('home')
			elif request.POST['action'] == 'Catering':
				form =  EventRegistration.objects.get(id=pk)
				form.Catering = 'not_enroll'
				form.save()
				return redirect('home')
			elif request.POST['action'] == 'Projector':
				form =  EventRegistration.objects.get(id=pk)
				form.Projector = 'not_enroll'
				form.save()
				return redirect('home')
			elif request.POST['action'] == 'Decoration':
				form =  EventRegistration.objects.get(id=pk)
				form.Decoration = 'not_enroll'
				form.save()
				return redirect('event_working_on')
			elif request.POST['action'] == 'Photographer':
				form =  EventRegistration.objects.get(id=pk)
				form.Photographer = 'not_enroll'
				form.save()
				return redirect('home')

	posts = {'events':EventRegistration.objects.filter(id=pk),}
	return render(request, 'events/manager-event-view-form.html',posts)

def EventWorkingOnView(request):
	if request.user.is_authenticated:
		posts = {'events':EventRegistration.objects.all()}
		return render(request, 'events/Events-working-on.html',posts)
	else:
		messages.success(request,' Please Login First ')

def Feedback(request):
	if request.method == 'POST':
		name = request.POST['fullname']
		mobile = request.POST['userphone'] 
		email = request.POST['useremail']
		subject = request.POST['usersubject']
		message = request.POST['Message']
		data = FeedBack.objects.create(full_name=name,email=email,mobile_no=mobile,subject=subject,message=message)
		data.save()
		messages.success(request, 'Success ! Your message has been sent..  ')
		return redirect('/')
	return render(request, 'events/index.html')

	