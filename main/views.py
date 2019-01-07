# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse
import json
import time
import datetime
from .models import *
from django.http import Http404
from django.utils.html import strip_tags
from django.views.generic import ListView
from django.utils.html import escape
from elasticsearch import Elasticsearch

# Create your views here.

__all__ = (
	'Index',
	'PoiRequest',
	'DragPoi',
)



class Index(TemplateView):
	template_name = 'main/index.html'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		return context





#https://192.168.33.10:8000/poi/?lat=60.000&lon=30.000
class PoiRequest(View):
	def get(self, request,**kwargs):
		result = {}

		lat = request.GET['lat']
		lng = request.GET['lon']
		geo = lat + ',' + lng
		es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
		points= es.search(index='poi', doc_type='points', body={"size": 2000, "query":{"bool" : {"filter": {"geo_distance": {"location": geo, "distance" : "10km"}}}}})		

		items = []
		for hit in points['hits']['hits']:
			item = {}
			item['id'] = hit['_id']
			item['title'] = hit['_source']['title']
			item['address'] = hit['_source']['address']
			item['city'] = hit['_source']['city']
			item['country'] = hit['_source']['country']
			item['type'] = hit['_source']['poi_type']
			item['lat'] = hit['_source']['location']['lat']
			item['lon'] = hit['_source']['location']['lon']
			items.append(item)

		result['points'] = items

		result['res'] = 'ok'
		response = JsonResponse(result, safe=False)
		return response





#https://192.168.33.10:8000/get_draged/?top_left_lat=60.05623261058863&top_left_lon=29.923147685791037&bottom_right_lat=59.91885202490504&bottom_right_lon=30.465254314209005
class DragPoi(View):
	def get(self, request,**kwargs):
		result = {}

		top_left_lat = request.GET['top_left_lat']
		top_left_lon = request.GET['top_left_lon']
		bottom_right_lat = request.GET['bottom_right_lat']
		bottom_right_lon = request.GET['bottom_right_lon']

		top_left = top_left_lat + ',' + top_left_lon
		bottom_right = bottom_right_lat + ',' + bottom_right_lon
		es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
		points= es.search(index='poi', doc_type='points', body={"size": 2000, "query":{"bool" : {"filter": {"geo_bounding_box": {"location": {"top_left": top_left, "bottom_right": bottom_right}}}}}})		

		items = []
		for hit in points['hits']['hits']:
			item = {}
			item['id'] = hit['_id']
			item['title'] = hit['_source']['title']
			item['address'] = hit['_source']['address']
			item['city'] = hit['_source']['city']
			item['country'] = hit['_source']['country']
			item['type'] = hit['_source']['poi_type']
			item['lat'] = hit['_source']['location']['lat']
			item['lon'] = hit['_source']['location']['lon']
			items.append(item)

		result['points'] = items

		result['res'] = 'ok'
		response = JsonResponse(result, safe=False)
		return response