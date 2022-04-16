from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile


def CreateProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile = Profile.objects.create(
            User_name = user,
            First_name = user.first_name,
            Last_name = user.last_name,
            Email = user.email,
        )

def Updateuser(sender,instance,created,**kwargs):
    print ('user updated!')
    profile = instance
    user = profile.User_name
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.save()

def deleteuser(sender, instance, **kwargs):
    print ('user deleted!')
    user = instance.User_name
    user.delete()

post_save.connect(CreateProfile,sender=User)
post_save.connect(Updateuser,sender=Profile)
post_delete.connect(deleteuser, sender=Profile)