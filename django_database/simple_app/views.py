from http.client import HTTPResponse
from re import template
from unittest import TestProgram
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from django.template import loader

# Create your views here.
def index(request):
    latest_notes_list = Note.objects.order_by('-day')[:5]
    template = loader.get_template('simple_app/index.html')

    context = {
        'latest_notes_list': latest_notes_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, note_id):
    note = Note.objects.get(pk=note_id)

    template = loader.get_template('simple_app/detail.html')

    context = {
        'note': note
    }

    return HttpResponse(template.render(context, request))
