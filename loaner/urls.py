from django.urls import path

from loaner import views

urlpatterns = [
    path('loaner/', views.Loaner, name='loaner'),
    # path('validate/', views.validate_email, name='validate_email'),
    # path('website/', views.index, name='index'),
    # # path('<pk>', SubscribeDetailView.as_view()),

    # path('about/', views.about, name="about"),
    # path('service/', views.service, name="service"),
    # path('testimonial/', views.testimonial, name='testimonial'),
    # path('contact/', views.Contact, name="contact"),
]
