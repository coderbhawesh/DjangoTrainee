#Question 1
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received. Processing...")
    time.sleep(5)  # Simulate a time-consuming task
    print("Processing complete.")

# Simulate saving a User instance
new_user = User(username='testuser')
new_user.save()
print("User save operation complete.")

