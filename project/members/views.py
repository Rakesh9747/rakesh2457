from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'members': mydata,
  }
  return HttpResponse(template.render(context, request))

def hema(request):
  mydata = Member.objects.filter(firstname='HEMA').values()
  template = loader.get_template('template.html')
  context = {
    'members': mydata,
  }
  return HttpResponse(template.render(context, request))

def Descending(request):
  mydata = Member.objects.all().order_by('-firstname').values()
  template = loader.get_template('template.html')
  context = {
    'members': mydata,
  }
  return HttpResponse(template.render(context, request))
