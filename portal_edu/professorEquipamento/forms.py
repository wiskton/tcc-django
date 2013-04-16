from django import forms
from professorEquipamento.models import ProfessorEquipamento

class FormProfessorEquipamento(forms.ModelForm):
	class Meta:
		model = ProfessorEquipamento