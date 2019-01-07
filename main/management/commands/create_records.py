# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import os
from elasticsearch import Elasticsearch

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elastic.settings")

from main.models import (
    Poi,
)



class Command(BaseCommand):

    def handle(self, *args, **options):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        count = 0
        for p in Poi.objects.all().order_by('id'):            
            
            count = count + 1
            doc = {
                'title':p.title,
                'address':p.address,
                'city':p.city, 
                'country':p.country,
                'poi_type':p.poi_type,
                'location':{'lat': p.lat, 'lon': p.lng}
            }
            
            
            res = es.index(index='poi', doc_type='points', body=doc, id=p.id)
            print("poi id "+ str(p.id))
            print("count "+str(count))
            print("***********************")
            