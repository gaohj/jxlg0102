from django.shortcuts import render,redirect,reverse
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.

def index(request):
    # html = render_to_string('index1html')
    # return HttpResponse(html)
    return render(request, 'index.html')
