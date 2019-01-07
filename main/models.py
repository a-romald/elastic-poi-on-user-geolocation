# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

__all__ = (
	'Poi',
)


class Poi(models.Model):
    title = models.CharField(u'Title', max_length=255)
    address = models.CharField(u'Address', max_length=512, blank=True, null=True)
    city = models.CharField(u'City', max_length=255, blank=True, null=True)
    country = models.CharField(u'Country', max_length=255, blank=True, null=True)
    poi_type = models.CharField(u'Type of poi', max_length=255, blank=True, null=False)  
    lat = models.DecimalField(u'Latitide', max_digits=10, decimal_places=6, null=True, blank=False)
    lng = models.DecimalField(u'Longitude', max_digits=10, decimal_places=6, null=True, blank=False)
    add_time = models.DateTimeField(u'Add datetime', auto_now_add=True)
    
    class Meta:
        verbose_name = u'Point of interest'
        verbose_name_plural = u'Points of interest'
        ordering = ['title']
        unique_together = (('lat', 'lng',),)

    def __str__(self):
        return self.title