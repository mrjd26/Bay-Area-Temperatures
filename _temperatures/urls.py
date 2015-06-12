from django.conf.urls import patterns, url
from _temperatures import views

urlpatterns = patterns('',
	
	url(r'^$',views.index,name='index'),
)
