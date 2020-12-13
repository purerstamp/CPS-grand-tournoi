from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('listing/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
# Create your views here.
