from django.shortcuts import render_to_response
from django.template import RequestContext
from equipamento.models import Equipamento
from forms import FormProfessorEquipamento
from models import ProfessorEquipamento

DIR = 'equipamento/'

def reservarEquipamento(request, id_equipamento):

  if request.method == 'POST':
    form = FormProfessorEquipamento(request.POST)
    if form.is_valid():
      form.enviado = True
      professorEquipamento = form.save()
      return render_to_response(DIR + 'agendado.html', {'professorEquipamento': professorEquipamento})

  else:
    form = FormProfessorEquipamento()

  VARS = {
    'form':form,
  }
	
  try:
    equipamento = Equipamento.objects.get(id=id_equipamento)
    return render_to_response(DIR + 'reservar.html', 
    {'form': form, 'professor': request.session['professor'], 'equipamento': equipamento}, 
    context_instance=RequestContext(request))
  except:
    return render_to_response(DIR + 'erro.html', {'erro': 'Equipamento não encontrado.'})