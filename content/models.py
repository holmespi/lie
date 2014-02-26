from django.db import models


# Create your models here.

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

	def __unicode__(self):
		return self.title



class Product(models.Model):
	stock = models.BooleanField()
	name = models.CharField(max_length=128, unique=True)
	price = models.IntegerField()
	description = models.TextField()
	category = models.ManyToManyField(Categories)
	size = models.CharField(max_length=128, unique=True)

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
	link = models.URLField(max_length=200)
	products = models.ManyToManyField(Product)

	def __unicode__(self):
		return self.name



