from django.contrib import admin
from blog.models import Post
from blog.models import Product
from blog.models import Stockist

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','date')

admin.site.register(Post, PostAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

admin.site.register(Product, ProductAdmin)

class StockistAdmin(admin.ModelAdmin):
	list_display = ('name','location')

admin.site.register(Stockist, StockistAdmin)