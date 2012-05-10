from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'items.views.items'),
     #url(r'^foodscouts/', include('foodscouts.foo.urls')),
	 url(r'^my_recommendations/(?P<user_id>\d+)/$', 'items.views.recommendations'),
	 url(r'^my_reviews/(?P<user_id>\d+)/$', 'items.views.my_reviews'),
	 url(r'^my_bookmarks/(?P<user_id>\d+)/$', 'items.views.my_bookmarks'),
	 url(r'^reviews/(?P<item_id>\d+)/$', 'items.views.reviews'),
    #url(r'^average/(?P<item_id>\d+)/$', 'items.views.average'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
