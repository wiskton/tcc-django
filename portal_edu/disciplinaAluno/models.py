# -*- coding: utf-8 -*-
from django.db import models

class DisciplinaAluno(models.Model):
	disciplina_id = models.ForeignKey('disciplina.Disciplina',null=False)
	aluno_id = models.ForeignKey('aluno.Aluno',null=False)
	turma_id = models.ForeignKey('turma.Turma',null=False)
	nota1 = models.DecimalField(max_digits=4,decimal_places=2,default=0,null=False)
	nota2 = models.DecimalField(max_digits=4,decimal_places=2,default=0,null=False)
	exame = models.DecimalField(max_digits=4,decimal_places=2,default=0,null=False)
	falta = models.DecimalField(max_digits=4,decimal_places=2,default=0,null=False)
	
	class Meta:
		db_table = 'disciplina_aluno'
		
	def __unicode__(self):
		return str(self.disciplina_id.nome) + ' - ' + self.aluno_id.nome + ' - ' + self.turma_id.nome