from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.HomePageView,name="home"),
    path('event-registration/', views.EventPageView,name="book"),
    path('eventportal/', views.EventPortalView,name="eventportal"),
 	path('event-working-on/', views.EventWorkingOnView,name="event_working_on"),
 	path('manager-event-view/<str:pk>', views.ManagerEventViewForm,name="manager_event_view_form"),
 	path('feedback/', views.Feedback,name="feedback"), 
]