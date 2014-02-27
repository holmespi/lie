from django.db import models

# Create your models here.

class Slider(models.Model):
	test = models.CharField(max_length=128, null=True, blank=True)
	images = models.FileField(upload_to="slider_images")

class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __unicode__(self):
        return self.category

    class Meta:
        ordering = ('category',)

class Post(models.Model):
	title = models.CharField(max_length=128, unique=True)
	date = models.DateField(auto_now=True)
	description = models.TextField()
	photo = models.FileField(upload_to='news') #change this to a URLField for production or else find a way to manage ftp uploads from django admin

	def __unicode__(self):
		return self.title



class Product(models.Model):
	stock = models.BooleanField()
	thumb = models.FileField(upload_to='products') #change this to a URLField for production or else find a way to manage ftp uploads from django admin 
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(max_length=128, unique=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField()
	category = models.ManyToManyField(Categories)
	size = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name


class Stockist(models.Model):
	name = models.CharField(max_length=128)
	website = models.URLField(max_length=200)
	location = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name



class Collection(models.Model):
	name = models.CharField(max_length=128)
	photo = models.FileField(upload_to='collections') #change this to a URLField for production or else find a way to manage ftp uploads from django admin
	link = models.URLField(max_length=200)
	products = models.ManyToManyField(Product)

	def __unicode__(self):
		return self.name



