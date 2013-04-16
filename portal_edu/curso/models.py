from django.db import models

class Curso(models.Model):
	nome = models.CharField(max_length=150,null=False)

	class Meta:
		db_table = u'curso'
		
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome