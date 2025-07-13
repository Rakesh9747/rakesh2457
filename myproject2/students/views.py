from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Student
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'students': mydata,
  }
  return HttpResponse(template.render(context, request))

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'roll_number', 'email', 'date_of_birth']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student_list.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'roll_number', 'email', 'date_of_birth']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
