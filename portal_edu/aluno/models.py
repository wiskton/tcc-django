from django.db import models

class Aluno(models.Model):
	nome = models.CharField(max_length=100,null=False)
	login = models.CharField(max_length=45,null=False,unique=True)
	senha = models.CharField(max_length=45,null=False)
	
	class Meta:
		db_table = u'aluno'
		verbose_name = u'Aluno'
		verbose_name_plural = u'Alunos'
	
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome