# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Disciplina

DIR = 'disciplina/'

def disciplinasProfessor(request):
	id_professor = request.session['professor'].id
	lista_disciplinas = Disciplina.objects.filter(professor_id=id_professor)
	return render_to_response(DIR + 'disciplina.html', {'lista_disciplinas' : lista_disciplinas})