from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyWeb.views.home', name='home'),
    # url(r'^MyWeb/', include('MyWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'apps.account.views.login'),
    url(r'^accounts/logout/$', 'apps.account.views.logout'),
    url(r'^search/$', 'apps.account.views.contact'),
)
