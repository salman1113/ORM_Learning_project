from .models import Students
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save, sender=Students)
def student_created(sender, instance, created, **kwargs):
    if created:
        print("signals fired new student created:", instance.name)


        if instance.email:
            subject = "Welcome Student!"
            message = f"Hi {instance.name}, Your student account has been created."
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["test@gmail.com"],
                fail_silently=True,
            )

@receiver(pre_save, sender=Students)
def student_pre_save(sender, instance, **kwargs):
    print("pre save signal this about to save:", instance.name)

@receiver(post_delete, sender=Students)
def student_post_delete(sender, instance, **kwargs):
    print("Post Delete Student deleted:", instance.name)


    #aggregate, annotate practical
    #select-related, prefetch_related
    #Q,F
    #practicals