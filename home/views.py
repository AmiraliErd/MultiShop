from django.shortcuts import render
from django.views.generic import TemplateView
from cart.models import Order


class Home(TemplateView):
    template_name = "home/index.html"


