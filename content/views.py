# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
	context = RequestContext(request)

	return render_to_response('home.html', context)


def store(request):
	context = RequestContext(request)

	return render_to_response('store.html', context)


def deadstock(request):
	context = RequestContext(request)
	
	return render_to_response('deadstock.html', context)

def news(request):
	context = RequestContext(request)

	return render_to_response('news.html', context)

def contact(request):
	context = RequestContext(request)

	return render_to_response('contact.html', context)

def collections(request):
	context = RequestContext(request)

	return render_to_response('collections.html', context)

def stockists(request):
	context = RequestContext(request)

	return render_to_response('stockists.html', context)
