from django.shortcuts import render , get_object_or_404
# from django.http import HttpResponse, JsonResponse

from .models import Articles
import logging

# Create your views here.
def home(request):
    context = {
        # "articles": Articles.objects.all()
        "articles": Articles.objects
                        .filter(status="p")
                        .order_by("-publish")[:3]
    }
    return render(request, "blog/home.html", context)


def detail(request, slug):
    context = {
        # "article":  Articles.objects.get(slug=slug)
        "article" : get_object_or_404(Articles , slug=slug)
    }
    return render(request, "blog/detail.html", context)


