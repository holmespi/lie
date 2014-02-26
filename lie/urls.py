from django.conf.urls import patterns, include, url
from content import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lie.views.home', name='home'),
    # url(r'^lie/', include('lie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),

	url(r'^collections/', views.collections, name='collections'),

	url(r'^contact/', views.contact, name='contact'),

	url(r'^deadstock/', views.deadstock, name='deadstock'),

	url(r'^news/', views.news, name='home'),

	url(r'^stockists/', views.stockists, name='stockists'),

	url(r'^store/', views.store, name='store'),


)
