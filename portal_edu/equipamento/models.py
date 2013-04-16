# -*- coding: utf-8 -*-
from django.db import models

class Equipamento(models.Model):
	STATUS_CHOICES = (
	    ('D', 'Disponível'),
	    ('I', 'Indisponível'),
	    ('M', 'Manutenção'),
	)
	nome = models.CharField(max_length=100,null=False)
	cod_patrimonio = models.CharField(max_length=100,null=False)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	class Meta:
		db_table = u'equipamento'
		
	def __unicode__(self):
		return str(self.id) + ' - ' + self.nome