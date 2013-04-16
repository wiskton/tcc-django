from django.db import models

class ProfessorEquipamento(models.Model):
	professor_id = models.ForeignKey('professor.Professor',null=False)
	equipamento_id = models.ForeignKey('equipamento.Equipamento',null=False)
	data_inicial = models.DateTimeField(null=False)
	data_final = models.DateTimeField(null=False)
	sala = models.CharField(max_length=3,null=False)
	
	class Meta:
		db_table = u'professor_equipamento'
		
	def __unicode__(self):
		return str(self.professor_id.nome) + ' - ' + self.equipamento_id.nome