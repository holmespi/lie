# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.syndication.views import Feed
from content.models import Slider
from content.models import Product
from content.models import Post
from content.models import Collection


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

	product_list = Product.objects.filter(stock=True)
	context_dict = {
	'page_title': 'Love is Earth - Store',
	'page_desc': 'Welcome to the store, here you can purchase LIE merchandise.  We will ship directly from our headquarters in the USA to you.',
	'page_type': 'product',
	'page_image': ''
	}
	context_dict['products'] = product_list
	return render_to_response('store.html', context_dict, context)

def product_single(request, slug):
	context = RequestContext(request)

	product = get_object_or_404(Product, slug=slug)
	context_dict = {
	'page_title': 'Love is Earth - Store - %s' % product.name,
	'page_desc': 'Welcome to the store, here you can purchase LIE merchandise.  We will ship directly from our headquarters in the USA to you.',
	'page_type': 'product',
	'page_image': ''
	}
	context_dict['product'] = product
	return render_to_response('product_single.html', context_dict, context)

def deadstock(request):
	context = RequestContext(request)

	product_list = Product.objects.filter(stock=False)
	context_dict = {
	'page_title': 'Love is Earth - Deadstock',
	'page_desc': 'The Deadstock - Check out the past items we have released.  LIE does not relaunch items, so be sure to head to the store and get what you can, while you can!',
	'page_type': 'blog',
	'page_image': ''
	}
	context_dict['products'] = product_list	
	return render_to_response('deadstock.html', context_dict, context)

def news(request):
	context = RequestContext(request)

	post_list = Post.objects.order_by('-id')
	context_dict = {
	'page_title': 'Love is Earth - News',
	'page_desc': 'Featured news for Love is Earth.  Find any upcoming events, shows, new releases, sale information.',
	'page_type': 'blog',
	'page_image': ''
	}
	context_dict['posts'] = post_list

	return render_to_response('news.html', context_dict, context)

def news_single(request, slug):
	context = RequestContext(request)

	post = get_object_or_404(Post, slug=slug)
	context_dict = {
	'page_title': 'Love is Earth - News - %s' % post.title,
	'page_desc': 'Featured news for Love is Earth.  Find any upcoming events, shows, new releases, sale information.',
	'page_type': 'blog',
	'page_image': ''
	}
	context_dict['post'] = post

	return render_to_response('news_single.html', context_dict, context)

def contact(request):
	context = RequestContext(request)

	return render_to_response('contact.html', context)

def collections(request):
	context = RequestContext(request)

	collection_list = Collection.objects.order_by('-id')
	context_dict = {
	'page_title': 'Love is Earth - Collections',
	'page_desc': 'Find the media from all our collection releases below.',
	'page_type': 'blog',
	'page_image': ''
	}
	context_dict['collections'] = collection_list

	return render_to_response('collections.html', context_dict, context)

def stockists(request):
	context = RequestContext(request)

	return render_to_response('stockists.html', context)


##Feeds

class latestNews(Feed):
	title = 'Love is Earth - News Feed'
	link = '/news/'
	description = 'The latest news and updates from Love is Earth'

	def items(self):
		return Post.objects.order_by('-id')

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description

	def item_link(self, item):
		return reverse('news-item', args=[item.pk])










