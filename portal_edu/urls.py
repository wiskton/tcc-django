from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'home.views.index'),
	(r'^aluno/$', 'aluno.views.login'),
	(r'^aluno/logout/$', 'aluno.views.logout'),
	(r'^aluno/disciplina/$', 'disciplinaAluno.views.disciplinasAluno'),
	(r'^professor/$', 'professor.views.login'),
	(r'^professor/logout/$', 'professor.views.logout'),
	(r'^professor/material/$', 'material.views.material'),
	(r'^professor/material/adiciona/$', 'material.views.adiciona'),
	(r'^professor/equipamento/$', 'equipamento.views.equipamento'),
	(r'^professor/disciplina/$', 'disciplina.views.disciplinasProfessor'),
	(r'^professor/disciplina/(?P<id_disciplina>\d+)/$', 'disciplinaAluno.views.disciplinasAlunos'),
	(r'^professor/nota/aluno/(?P<id_disciplinaAluno>\d+)/$', 'disciplinaAluno.views.alterarNotaAluno'),
	(r'^professor/equipamento/(?P<id_equipamento>\d+)/$', 'professorEquipamento.views.reservarEquipamento'),
    (r'^admin/', include(admin.site.urls)),
)
