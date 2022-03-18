from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video
import os

@receiver(post_delete, sender=Video)
def delete_video_files_after_delete_instance(sender, instance, *args, **kwargs):
    try:
        file_path = instance.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
    except BaseException:
        pass
