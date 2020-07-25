from . import views
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path('weather_or_not/', include('weather_or_not.urls'), name="weather"),
]