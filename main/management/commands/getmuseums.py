# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import os
import csv
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elastic.settings")

from main.models import (
	Poi,    
)

# SCRIPT TO UPLOAD MUSEUMS FROM CSV-FILE

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		
		with open('/vagrant/elastic/main/data/museums.csv', 'r') as mydata:
			i = 0			
			csvreader = csv.reader(mydata, delimiter=',')
			next(csvreader) # skip header
			for line in csvreader:
				if i < 100000 :					
					name = line[0]
					country = line[5]
					city = line[6]
					lat = line[7]
					lon = line[8]					
					
					try:
						if name != '':
							poi = Poi.objects.create(title=name, location=city, country=country, poi_type='museum', lat=lat, lng=lon)
							poi.save()						
					except:
						pass
					
					i += 1
					print(str(i) + '. ' + name + ' - ' + lat + ':' + lon)
					sleep(0.1)

		self.stdout.write('Done!\n')