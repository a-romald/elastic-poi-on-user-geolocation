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
		created = False
		# index settings
		settings = {
			"settings": {
				"number_of_shards": 1,
				"number_of_replicas": 0
			},
			"mappings": {
				"points": { #doc_type
					"dynamic": "strict",
					"properties": {						
						"title": {
							"type": "text"
						},
						"address": {
							"type": "text"
						},
						"city": {
							"type": "text"
						},
						"country": {
							"type": "text"
						},
						"poi_type": {
							"type": "text"
						},
						"location": {
							"type": "geo_point"
						},
					}
				}
			}
		}

		try:
			es_object = Elasticsearch([{'host': 'localhost', 'port': 9200}])
			if not es_object.indices.exists('poi'):
				# Ignore 400 means to ignore "Index Already Exist" error.
				es_object.indices.create(index='poi', ignore=400, body=settings)
				print('Created Index')
			created = True
		except Exception as ex:
			print(str(ex))
		finally:
			print(str(created))
