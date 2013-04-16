# -*- coding: utf-8 -*-
from django import forms
from material.models import Material

class FormMaterial(forms.ModelForm):
	class Meta:
		model = Material
		exclude = ('data',)