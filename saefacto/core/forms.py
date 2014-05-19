# -*- coding: utf8 -*-
from django import forms
from parsley.decorators import parsleyfy
from core.models import Aluno


@parsleyfy
class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno


