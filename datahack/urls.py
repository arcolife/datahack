# project wide urls
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import visualizer.urls
import settings

# import your urls from each app here, as needed 

urlpatterns = patterns('',
                       url(r'^', include(visualizer.urls)),
                       #url(r'^admin/', include(admin.site.urls)),
                       #url(r'^mortality/', 'visualizer.views.mortality'),
                       #(r'^visualizer/', 'visualizer.views.visualizer'),
                       #url(r'^.*/$', TemplateView.as_view(template_name="home.html")),
                   )
