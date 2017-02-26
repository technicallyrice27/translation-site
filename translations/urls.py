from django.conf.urls import url

from . import views
from translations.feeds import LatestChapters
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^projects/', views.projects, name="projects"),
    url(r'^counterstop/', views.counterstop, name="counterstop"),
    url(r'^table_of_contents/(?P<ppk>\d+)/$', views.table_of_contents, name="table_of_contents"),
    url(r'^news/', views.news, name="news"),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^chapter/(?P<pk>\d+)/$', views.chapter_display, name='chapter_display'),
    #RSS
    url(r'^latest/chapters/$', LatestChapters(), name='rss')
]