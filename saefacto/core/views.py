from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from .forms import AlunoForm
from .models import Aluno


class AlunoView(generic.CreateView):
    model = Aluno
    #template_name = 'smartadmin/blank_.html'
    template_name = 'aaaa.html'
    form_class = AlunoForm
    success_url = '/'



