from django.db import models

class Turma(models.Model):
	nome = models.CharField(max_length=150,null=False)
	
	class Meta:
		db_table = u'turma'
		
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome