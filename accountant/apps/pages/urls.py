from django.conf.urls import patterns, url

from . import views

from stronghold.decorators import public


urlpatterns = patterns('',
    url(r'^$',
        public(views.HomeView.as_view()),
        name="home"),
)
