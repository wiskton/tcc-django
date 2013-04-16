# -*- coding: utf-8 -*-
from django.db import models

class Material(models.Model):
	nome = models.CharField(max_length=100,null=False)
	descricao = models.TextField()
	data = models.DateTimeField(auto_now_add=True)
	arquivo = models.FileField(upload_to='material')
	disciplina_id = models.ForeignKey('disciplina.Disciplina')
	
	class Meta:
		db_table = u'material'
		ordering = ["data"]
		verbose_name = u"Material"
		verbose_name_plural = u"Materiais"
		
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome