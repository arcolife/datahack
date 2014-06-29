# app specific urls
from django.conf.urls import patterns, include, url
#from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
                       #(r'^mortality/', TemplateView.as_view(template_name="heatmap.html")),
                       #(r'^visualizer/', TemplateView.as_view(template_name="index.html")),
                       (r'^$', TemplateView.as_view(template_name="index.html")),
                   )

