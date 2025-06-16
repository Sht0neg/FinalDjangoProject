from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_query_name="profile")
    role = models.BooleanField(verbose_name="Роль пользователя", blank=True, default=False)
    phone = models.CharField(verbose_name="Номер телефона", max_length=50, blank=True)

    def parse_object(self):
        return{
            "id": self.id,
            "name": self.user.username.split("/")[0],
            "second_name": self.user.first_name,
            "last_name": self.user.last_name,
            "role": self.role,
            "phone": self.phone
        }

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
