# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Professor
from django.template import RequestContext

DIR = 'professor/'

def login(request):
	if request.session.get('professor', False):
		return render_to_response(DIR + 'professor.html', {'professor' : request.session['professor']}, context_instance=RequestContext(request))
			
	if request.method == "POST":
		login = request.POST['login']
		senha = request.POST['senha']
		
		if login == "" or senha == "":
			return render_to_response(DIR + "erro.html", {})
		else:
		
			try:
				p = Professor.objects.get(login=login,senha=senha)
				request.session['professor'] = p
				return render_to_response(DIR + 'professor.html', { 'professor' : request.session['professor'] }, context_instance=RequestContext(request))
			except:
				return render_to_response(DIR + 'erro.html', {} )
	else:
		form = Professor();
		
	return render_to_response(DIR + "login.html", {'form': form}, context_instance=RequestContext(request))
		
def logout(request):
	try:
		del request.session['professor']
	except KeyError:
		pass
	return render_to_response(DIR + "sair.html", {})
