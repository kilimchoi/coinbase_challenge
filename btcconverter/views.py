import requests
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def order_book():
	r = requests.get("https://www.bitstamp.net/api/order_book")
	if r.status_code == 200:
		json_response = r.json()
		ask_length = len(json_response['asks'])
		bid_length = len(json_response['bids'])
		#return json_response['bids'][0], json_response['bids'][bid_length - 1]
		#return json_response['asks'][0], json_response['asks'][1], json_response['asks'][length-1]
		return json_response

	else:
		r.raise_for_status()

def get_bids(request):
	json_response = order_book()
	dict = {'bids': json_response['bids']}
	return render_to_response('static/index.html', dict, context_instance=RequestContext(request))

def get_asks(request):
	json_response = order_book()
	dict = {'asks': json_response['asks']}
	return render_to_response('static/index.html', dict, context_instance=RequestContext(request))


