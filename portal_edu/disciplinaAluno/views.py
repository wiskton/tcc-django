# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import DisciplinaAluno
from django.template import RequestContext
from forms import FormDisciplinaAluno
#from models import Aluno

DIR = 'nota/'
	
def disciplinasAluno(request):

	id_aluno = request.session['aluno'].id
	lista_disciplinas = DisciplinaAluno.objects.filter(aluno_id=id_aluno)
	return render_to_response(DIR + 'disciplina.html', {'lista_disciplinas' : lista_disciplinas}, context_instance=RequestContext(request))

def disciplinasAlunos(request, id_disciplina):

	try:
		lista_disciplinasAlunos = DisciplinaAluno.objects.filter(disciplina_id=id_disciplina)
	except:
		pass
	return render_to_response(DIR + 'nota.html', {'lista_disciplinasAlunos' : lista_disciplinasAlunos}, context_instance=RequestContext(request))

#def aluno(id_aluno):
#	aluno = Aluno.objects.get(id=id_aluno)
#	return aluno


def alterarNotaAluno(request, id_disciplinaAluno):
	
	if request.method == 'POST':
		form = FormDisciplinaAluno(request.POST)
		if form.is_valid():
			#a = DisciplinaAluno.objects.get(request.POST.get('id'))
			#disciplinaAluno = FormDisciplinaAluno(request.POST, instance=a)
			#disciplinaAluno.save()
			disciplinaAluno = form.save()
			return render_to_response(DIR + 'salvo.html', {'disciplinaAluno':disciplinaAluno}, context_instance=RequestContext(request))
		else:
			print "erro"

	else:
		form = FormDisciplinaAluno()

	VARS = {
		'form':form,
	}
        
	# lista dados do aluno
	aluno = DisciplinaAluno.objects.get(pk=id_disciplinaAluno)

	return render_to_response(DIR + "altera_nota_aluno.html", {'form': form, 'aluno' : aluno}, context_instance=RequestContext(request))
