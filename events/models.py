from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class EventRegistration(models.Model):
    status = (

    ('not_enroll', 'Not Enroll'),
    ('need_to_work', 'NEED TO WORK'),
    ('in_process', ' IN PROCESS'),
    ('done', 'DONE'),
    )

    Event_Status = (

    ('accepted', 'accepted'),
    ('pending', 'pending'),
    ('reject','reject'),
    ('completed', 'completed'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='customer')
    manager = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='manager')
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name='customer_profile')
    manager_profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name='manager_profile')
    location = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30,null=True)
    state = models.CharField(max_length=30,null=True)
    event_date =  models.DateField(blank=True,null=True)
    budget = models.CharField(max_length=30,null=True)
    event_type = models.CharField(max_length=30,null=True)
    Sound_system = models.CharField(max_length=30,null=True,choices=status)
    Catering = models.CharField(max_length=30,null=True,choices=status)
    Projector = models.CharField(max_length=30,null=True,choices=status)
    Decoration = models.CharField(max_length=30,null=True,choices=status)
    Photographer = models.CharField(max_length=30,null=True,choices=status)
    confirmation = models.CharField(max_length=30,null=True,choices=Event_Status)
    confirmation_date = models.DateField(blank=True,null=True)
    comment = models.CharField(max_length=500,null=True)
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.event_type
    class Meta:
    	verbose_name_plural = "Event Portal"

class FeedBack(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=30)
    subject = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=300, null=True)
    register_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "FeedBack"

