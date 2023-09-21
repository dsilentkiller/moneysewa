from django.urls import path

from website import views

urlpatterns = [
    # path('subscribe/', views.Subscribe, name='subscribe'),
    path('validate/', views.validate_email, name='validate_email'),
    path('website/', views.index, name='index'),
    # path('<pk>', SubscribeDetailView.as_view()),

    path('about/', views.About, name="about"),
    path('service/', views.Service, name="service"),
    path('testimonial/', views.Testimonial, name='testimonial'),
    path('contact/', views.Contact, name="contact"),
]
