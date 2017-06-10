from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> a78ddea0a02171f34cb4356bc34b12f7bbfce4e4

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('mainapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
<<<<<<< HEAD

urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                    )
=======
>>>>>>> a78ddea0a02171f34cb4356bc34b12f7bbfce4e4
