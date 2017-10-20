from django.conf.urls import url

from . import views
app_name = 'obj'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^do_create/$', views.do_create, name='do_create'),
    url(r'^(?P<oid>.+?)/$', views.detail, name='detail'),
]
