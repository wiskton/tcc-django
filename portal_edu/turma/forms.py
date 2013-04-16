# -*- coding: utf-8 -*-
from django import forms
from turma.models import Turma

class FormTurma(forms.ModelForm):
	class Meta:
		model = Turma