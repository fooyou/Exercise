from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from .models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = context.Context({'posts': posts})
    return HttpResponse(t.render(c))
