from django.shortcuts import render_to_response
from models import Material
from django.template import RequestContext
from forms import FormMaterial
from disciplina.models import Disciplina
import datetime

DIR = 'material/'
	
def material(request):
	lista_materiais = Material.objects.all()
	return render_to_response(DIR + 'material.html', {'lista_materiais' : lista_materiais})

def adiciona(request):

	# lista todas disciplinas do professor
	id_professor = request.session['professor'].id
	disciplina = Disciplina.objects.filter(professor_id=id_professor)
	
	if request.method == 'POST':
		form = FormMaterial(request.POST, request.FILES)
		if form.is_valid():
			form.enviado = True
			material = form.save()
			return render_to_response(DIR + 'salvo.html', {})

	else:
		form = FormMaterial()

	VARS = {
		'form':form,
	}

	return render_to_response(DIR + "adiciona.html", 
	{'form': form, 'disciplina': disciplina}, 
	context_instance=RequestContext(request))