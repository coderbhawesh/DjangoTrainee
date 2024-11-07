from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # Modify the instance within the signal handler
    instance.name = "Modified"
    instance.save()

# Start a transaction
try:
    with transaction.atomic():
        # Create an instance of MyModel
        obj = MyModel.objects.create(name="Original")
        # Raise an exception to trigger a rollback
        raise Exception("Triggering rollback")
except Exception as e:
    print(f"Exception occurred: {e}")

# Check if the object exists in the database
exists = MyModel.objects.filter(name="Modified").exists()
print(f"Object with name 'Modified' exists: {exists}")
