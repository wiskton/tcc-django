# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Turma
from django.template import RequestContext
from forms import FormTurma
from django.shortcuts import get_object_or_404

DIR = 'turma/'

def turma(request):
	lista_turmas = Turma.objects.all()
	return render_to_response(DIR + 'turma.html', {'lista_turmas' : lista_turmas})