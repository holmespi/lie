# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from content.models import Slider

def home(request):
	context = RequestContext(request)

	slider_list = Slider.objects.all()
	context_dict = {
	'page_title': 'Love is Earth - Home',
	'page_desc': 'Love is Earth - Representing the dirty south trap vibe, with relevant streetwear and cultre',
	'page_type': 'website',
	'page_image': ''
	}
	context_dict['slides'] = slider_list
	return render_to_response('home.html', context_dict, context)


def store(request):
	context = RequestContext(request)
	context_dict = {
	'page_title': 'Love is Earth - Store',
	'page_desc': 'Love is Earth - Representing the dirty south trap vibe, with relevant streetwear and cultre',
	'page_type': 'website',
	'page_image': ''
	}
	return render_to_response('store.html', context_dict, context)


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
