# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
        template_name = 'index.html'
        msg='Hello welcome'


        contex={
        'Hello':msg,

        }
        return render(request, template_name,contex)
