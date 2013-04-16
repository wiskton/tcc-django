# -*- coding: utf-8 -*-
from django import forms
from equipamento.models import Equipamento

class FormEquipamento(forms.ModelForm):
	class Meta:
		model = Equipamento