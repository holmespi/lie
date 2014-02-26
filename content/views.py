# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def home(request):
	context = RequestContext(request)	

def store(request):
	context = RequestContext(request)

def deadstock(request):
	context = RequestContext(request)

def news(request):
	context = RequestContext(request)

def contact(request):
	context = RequestContext(request)

def collection(request):
	context = RequestContext(request)

def stockist(request):
	context = RequestContext(request)

