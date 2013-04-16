# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Equipamento
from django.template import RequestContext
from forms import FormEquipamento

DIR = 'equipamento/'

def equipamento(request):
	lista_equipamentos = Equipamento.objects.all()
	return render_to_response(DIR + 'equipamento.html', {'lista_equipamentos' : lista_equipamentos})
