from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.db.models.signals import post_save

from orders.models import Order
from .models import Robot


@receiver(post_save, sender=Robot)
def send_order_mail_signal(instance, created, **kwargs):
    if created:
        order = Order.objects.filter(robot_serial=instance.serial)

        if not order:
            return
        else:
            first_ord = order.first()
            rob = Robot.objects.filter(serial=first_ord.robot_serial).first()
            model = rob.model
            version = rob.version
            email = order.first().customer.email
            subj = """Order status"""
            text = f"""Добрый день!\nНедавно вы интересовались нашим роботом модели {model}, версии {version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."""

            email = EmailMessage(
                subject=subj,
                body=text,
                to=[email],
            )
            email.send()

            first_ord.delete()
