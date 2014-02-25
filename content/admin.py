from django.contrib import admin
from content.models import Post
from content.models import Product
from content.models import Stockist

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','date')

admin.site.register(Post, PostAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

admin.site.register(Product, ProductAdmin)

class StockistAdmin(admin.ModelAdmin):
	list_display = ('name','location')

admin.site.register(Stockist, StockistAdmin)