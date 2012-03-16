from inventory.models import *
from django.shortcuts import render_to_response

def index(request):

    component_list = component.objects.all()
    return render_to_response('templates/index.html', {'component_list': component_list})


def detail(request,component_id):
    component_detail = component.objects.get(pk=component_id)
    return render_to_response('templates/detail.html', {'component_detail': component_detail})
