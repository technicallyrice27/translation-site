from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from translations.feeds import LatestChapters
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^projects/(?P<pt>[-\w]+)/chapter/(?P<num>\d+)/$', views.chapter_display, name='chapter_display'),
    url(r'^projects/(?P<pt>[-\w]+)/$', views.project_page, name="project_page"),
    url(r'^projects/$', views.projects, name="projects"),
    url(r'^news/(?P<slug>[-\w]+)/$', views.post, name='post'),
    url(r'^news/', views.news, name="news"),
    url(r'^contact/', views.contact, name="contact"),
    #Old versions for redirects
    url(r'^post/(?P<pk>\d+)/$', views.post_old, name='post_old'),
    url(r'^table_of_contents/(?P<ppk>\d+)/$', views.table_of_contents_old, name="table_of_contents_old"),
    url(r'^chapter/(?P<pk>\d+)/$', views.chapter_display_old, name='chapter_display_old'),
    #RSS
    url(r'^latest/chapters/$', LatestChapters(), name='rss')
]