from rest_framework import serializers
from .models import SubscribedUsers, About, Testimonial, Contact, Info, Service


class SubscribedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedUsers
        fields = ('email', 'name', 'created_date')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'description']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'phone', 'message']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
