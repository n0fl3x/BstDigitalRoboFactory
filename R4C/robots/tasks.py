from celery import shared_task
from django.core.mail import EmailMessage

from .models import Robot
from orders.models import Order


@shared_task
def notify_order_robot_created(serial):
    order = Order.objects.filter(robot_serial=serial)

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
