from django.shortcuts import render

from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email',None)
        if not name or not email:
            messages.error(request, "you must type legit name and email to subscribe to a Newsletter")
        return redirect('/')
    
    if get_user_model().objects.filter(email=email).first():
        messages.error(request, "Found registered user with associated {email} email.You login to subscribe or unsubscribe.")
        