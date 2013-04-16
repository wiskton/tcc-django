from django.db import models

class Disciplina(models.Model):
	nome = models.CharField(max_length=100,null=False)
	professor_id = models.ForeignKey('professor.Professor')
	curso_id = models.ForeignKey('curso.Curso')
	
	class Meta:
		db_table = u'disciplina'
		
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome