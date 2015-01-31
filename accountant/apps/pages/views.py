import logging

from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class HomeView(generic.TemplateView):
    template_name = "pages/home.html"
