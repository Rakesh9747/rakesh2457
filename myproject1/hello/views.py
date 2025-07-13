from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  

def table(request):
    temp=loader.get_template('tables.html')