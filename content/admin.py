from django.contrib import admin
from content.models import Post
from content.models import Product
from content.models import Stockist
from content.models import Categories
from content.models import Collection


admin.site.register(Categories)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','date')

admin.site.register(Post, PostAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')

admin.site.register(Product, ProductAdmin)

class StockistAdmin(admin.ModelAdmin):
	list_display = ('name','location')

admin.site.register(Stockist, StockistAdmin)

class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name','id')

admin.site.register(Collection, CollectionAdmin)