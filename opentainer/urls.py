from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'', include('django.contrib.auth.urls')),
#        url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^web/', include('web.urls')),
        )

