from django import forms
from professor.models import Professor

class FormProfessor(forms.ModelForm):
	class Meta:
		model = Professor