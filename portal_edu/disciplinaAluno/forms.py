# -*- coding: utf-8 -*-
from django import forms
from disciplinaAluno.models import DisciplinaAluno

class FormDisciplinaAluno(forms.ModelForm):
	class Meta:
		model = DisciplinaAluno