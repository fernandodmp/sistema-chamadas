from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def placeholder(request):
    return HttpResponse("PLACEHOLDER VIEW")


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
