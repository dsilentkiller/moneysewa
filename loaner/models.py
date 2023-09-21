from django.db import models
from datetime import datetime


# Create your models here.


class PersonContact(models.Model):
    name = models.CharField(max_length=120)
    ntc_mobile = models.CharField(max_length=200)
    ncell_mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=300, choices=[('Male', 'Male'),
                                                       ('Female',
                                                        'Female'),
                                                       ], default='Male')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    marital_status = models.CharField(max_length=300, choices=[('Married', 'Married'),
                                                               ('Unmarried',
                                                               'Unmarried'),
                                                               ('single',
                                                               'single'),
                                                               ('divorced',
                                                               'divorced'),
                                                               ], default='Unmarried')
    government_id = models.CharField(max_length=300, choices=[('Citizenship', 'Citizenship'),
                                                              ('Password',
                                                               'Password'),
                                                              ('Driving License',
                                                               'Driving License'),

                                                              ], default='Citizenship')
    govproof_thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    personal_photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class DhitoDetails(models.Model):
    dito_type = models.CharField(max_length=300, choices=[('Gold', 'gold'),
                                                          ('Land',
                                                           'Land'),
                                                          ('House',
                                                           'House'),
                                                          ('Mobile',
                                                           'mobile'),
                                                          ('Car',
                                                           'Car'),
                                                          ('Bike/Scoty',
                                                           'Bike/Scoty'),

                                                          ], default='Mobile')
    bill = models.ImageField(upload_to='photos/%Y/%m/%d')
    dhito_picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    amount = models.CharField(max_length=400)
    valuation_rate = models.CharField(max_length=300, choices=[('20%', '20%'),
                                                               ('25%', '25%'),
                                                               ('30%', '30%'),
                                                               ('35%', '35%'),
                                                               ('40%', '40%'),
                                                               ('45%', '45%'),
                                                               ('50%', '50%'),
                                                               ('60%', '60%'),

                                                               ], default='30%')
    interest_rate = models.CharField(max_length=300, choices=[
        ('3.5%', '3.5%'),
        ('4%', '4%'),
        ('4.5%', '4.5%'),
        ('5%', '5%'),
        ('5.5%', '5.5%'),
        ('6%', '6%'),
        ('6.5%', '6.5%'),
        ('7%', '7%'),
        ('8%', '8%'),
        ('9%', '9%'),
        ('10%', '10%'),
        ('11%', '11%'),
        ('12%', '12%'),
        ('13%', '13%'),
        ('14%', '14%'),
        ('15%', '15%'),

    ], default='5%')
    duration = models.CharField(max_length=300, choices=[
        ('3day', '3 day'),
        ('5 day', '5day'),
        ('7 day', '7 day'),
        ('15 day', '15day'),
        ('30 day', '30 day'),
        ('60 day', '60 day'),
        ('90 day', '90 day'),
        ('120 day',
         '120 day'),
        ('150 day',
         '150day'),
        ('180 day',
         '180 day'),



    ], default='3 day')
    purpose = models.CharField(max_length=500)
    buying_price = models.CharField(max_length=600)
    secondhand_price = models.CharField(max_length=400)
    remark = models.CharField(max_length=500)


class Address(models.Model):
    province = models.CharField(max_length=200)
    district = models.CharField(max_length=300)
    municipility = models.CharField(max_length=400)
    ward_no = models.IntegerField()
    tole_name = models.CharField(max_length=400)
    per_longtitude = models.CharField(max_length=400)
    per_latitude = models.CharField(max_length=400)

    temp_province = models.CharField(max_length=200)
    temp_district = models.CharField(max_length=300)
    temp_municipility = models.CharField(max_length=400)
    temp_ward_no = models.IntegerField()
    temp_tole_name = models.CharField(max_length=400)
    temp_longtitude = models.CharField(max_length=400)
    temp_latitude = models.CharField(max_length=400)
