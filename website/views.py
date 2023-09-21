from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers
from django.shortcuts import render
from django.http import JsonResponse
import re
from .models import SubscribedUsers, About, Service, Testimonial, Contact
from django.core.mail import send_mail
from django.conf import settings
from .serializers import SubscribedUsersSerializer, AboutSerializer, ServiceSerializer, TestimonialSerializer, ContactSerializer
from rest_framework import viewsets


# Create your views here.
class SubscribedUsersView(viewsets.ModelViewSet):
    serializer_class = SubscribedUsersSerializer
    queryset = SubscribedUsers.objects.all()

    # def subscribe(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name', None)
    #         email = request.POST.get('email',None)
    #         if not name or not email:
    #             messages.error(request, "you must type legit name and email to subscribe to a Newsletter")
    #         return redirect('/')

    #     if get_user_model().objects.filter(email=email).first():
    #         messages.error(request, "Found registered user with associated {email} email.You login to subscribe or unsubscribe.")
    #         return redirect(request.META.get("HTTP_REFERER",'/'))

    #     subscribe_user = SubscribedUsers.objects.filter(email=email).first()
    #     if subscribe_user:
    #         messages.error(request, f"{email} email address is already subscriber.")
    #         return redirect(request.META.get("HTTP_REFERER",'/'))

    #     try:
    #         validate_email(email)
    #     except ValidationError as e:
    #         messages.error(request, e.messages[0])
    #         return redirect('/')

    #     subscribe_model_instance = SubscribedUsers()
    #     subscribe_model_instance.name = name
    #     subscribe_model_instance.email = email
    #     subscribe_model_instance.save()
    #     messages.success(request,f'{email} email was successfully subscribed to our newsletter !')
    #     return redirect(request.META.get("HTTP_REFERER",'/'))

    # def index(request):
    #     if request.method == 'POST':
    #         post_data = request.POST.copy()
    #         email = post_data.get('email', None)
    #         name = post_data.get('name', None)
    #         subscribedUsers = SubscribedUsers()
    #         subscribedUsers.email = email
    #         subscribedUsers.name = name
    #         subscribedUsers.save()

    #         # send a confirmation mail

    #         subject = 'Moneysewa Subscription'
    #         message = 'hello ' + name + \
    #             ', Thanks for subscribings us.You will get notificationof latest article posted on our website.please do not reply on this email.'
    #         email_from = settings.EMAIL_HOST_USER

    #         recipient_list = [email,]
    #         send_mail(subject, message, email_from, recipient_list)
    #         res = JsonResponse({'msg': 'Thanks. Subscribes Successfully!'})
    #         return res
    #     # need to change here
    #     return render(request, 'moneysewa')

    # def validate_email(request):
    # email = request.POST.get("email", None)
    # if email is None:
    #     res = JsonResponse({'msg': 'Emaail is required.'})
    # elif SubscribedUsers.objects.get(Email=email):
    #     res = JsonResponse({'msg': 'Email Address Already exists'})
    # elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
    #     res = JsonResponse({'msg': 'Invalid Email Address'})
    # else:
    #     res = JsonResponse({'msg': ''})
    # return res


class About(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    queryset = About.objects.all()


class Service(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class Testimonial(viewsets.ModelViewSet):
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.all()


class Contact(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
