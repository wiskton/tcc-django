# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Aluno
from django.template import RequestContext

DIR = 'aluno/'

def login(request):
	if request.session.get('aluno', False):
		return render_to_response(DIR + 'aluno.html', {'aluno' : request.session['aluno']}, context_instance=RequestContext(request))

	if request.method == "POST":
		login = request.POST['login']
		senha = request.POST['senha']

		if login == "" or senha == "":
			return render_to_response(DIR + "erro.html", {})
		else:

			try:
				a = Aluno.objects.get(login=login,senha=senha)
				request.session['aluno'] = a
				return render_to_response(DIR + 'aluno.html', { 'aluno' : request.session['aluno'] }, context_instance=RequestContext(request))
			except:
				return render_to_response(DIR + 'erro.html', {} )
	else:
		form = Aluno();

	return render_to_response(DIR + "login.html", {'form': form}, context_instance=RequestContext(request))

def logout(request):
	try:
		del request.session['aluno']
	except KeyError:
		pass
	return render_to_response(DIR + "sair.html", {})
