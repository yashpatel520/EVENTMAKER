from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	p_id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	middle_name = models.CharField(max_length=50, null=True,blank=True)
	mobile = models.CharField(max_length=10, unique=True,null=True,blank=True)
	usertype = models.CharField(blank=True,null=True,max_length=20)
	
	def __str__(self):
			return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()