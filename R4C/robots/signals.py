from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.db.models.signals import post_save

from orders.models import Order
from .models import Robot
from .tasks import notify_order_robot_created


@receiver(post_save, sender=Robot)
def send_order_mail_signal(instance, created, **kwargs):
    if created:
        notify_order_robot_created.delay(instance.serial)
        