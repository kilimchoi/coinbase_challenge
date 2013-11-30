import requests
import urllib2
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

def order_book():
	r = requests.get("https://www.bitstamp.net/api/order_book")
	if r.status_code == 200:
		json_response = r.json()
		json_response = simplejson.dumps(json_response)
		return json_response

	else:
		r.raise_for_status()

def index(request):
	json_response = order_book()
	dict = {'json_response': json_response}
	return render_to_response('static/index.html', dict, context_instance=RequestContext(request))


