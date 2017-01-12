from __future__ import unicode_literals

from django.db import models


class LiftUnit(models.Model):
    '''
    A single Access Platform Solution as a Vehicle or
    single unit.
    '''
    COST_TYPES = (
        ('sale', 'For Sale'),
        ('lease', 'For Hire'),
    )

    name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    cost = models.CharField(max_length=255, help_text='GBP')

    cost_type = models.CharField(
        max_length=10,
        choices=COST_TYPES,
        default='sale',
    )

    weight = models.IntegerField(help_text='KG Unit of measurement', blank=True, null=True)
    power = models.IntegerField(help_text='Horsepower Unit of measurement', blank=True, null=True)
    width  = models.IntegerField(help_text='CM Unit of measurement', blank=True, null=True)
    stow_height  = models.IntegerField(help_text='CM Unit of measurement', blank=True, null=True)
    platform_height = models.IntegerField(help_text='CM Unit of measurement', blank=True, null=True)
    platform_width = models.IntegerField(help_text='Unit of measurement', blank=True, null=True)
    platform_length = models.IntegerField(help_text='CM Unit of measurement', blank=True, null=True)
    working_height = models.IntegerField(help_text='CM Unit of measurement', blank=True, null=True)
    drive_speed = models.CharField(help_text='MPH', max_length=255, blank=True, null=True)
    capacity = models.IntegerField(help_text='KG Unit of measurement', blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'Lift Unit: %s' % self.name

