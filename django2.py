#Question2
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Simulate saving a User instance
new_user = User(username='testuser')
new_user.save()
print(f"Main thread ID: {threading.get_ident()}")
