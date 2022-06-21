from django.core.mail import send_mail
from django.conf import settings

def newAccount_email(email):
    # if new user is created
        send_mail(
            subject="Welcome to Isaac's Demo",
            message="Thanks for signing up for my demo project. This is an example of a welcome email!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )