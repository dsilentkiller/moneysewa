from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from website.models import SubscribedUsers
from django.shortcuts import render
from django.http import JsonResponse
import re
from .models import PersonContact, DhitoDetails, Address
from django.core.mail import send_mail
from django.conf import settings
from .serializers import PersonContactSerializer, DhitoDetailsSerializer, AddressSerializer
from rest_framework import viewsets


# Create your views here.
class PersonalContactView(viewsets.ModelViewSet):
    serializer_class = PersonContactSerializer
    queryset = PersonContact.objects.all()


class DhitoDetailsView(viewsets.ModelViewSet):
    serializer_class = DhitoDetailsSerializer
    queryset = DhitoDetails.objects.all()


class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class Loaner(viewsets.ModelViewSet):
    queryset = Address.objects.all()
