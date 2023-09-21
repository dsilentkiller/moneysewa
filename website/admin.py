from django.contrib import admin
from .models import SubscribedUsers, About, Info, Contact, Testimonial, Service

# class SubscribedUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name', 'created_date')

# admin.site.register(SubscribedUsers)

# class AboutAdmin(admin.ModelAdmin):
#     list_display = ('email','title','description','img')
admin.site.register(About)
admin.site.register(Service)


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('fullname','email','phone','message')
#     list_filter = ('is_admin')
#     search_fields =('fullname','email','phone')
admin.site.register(Contact)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display =('name','title','display')
admin.site.register(Testimonial)
# class InfoAdmin(admin.ModelAdmin):
#     list_display=('location','office_phone','office_email','office_media')


admin.site.register(Info)
