from django import forms
from .models import *

class EntradasForm(forms.ModelForm):
	class Meta:
		model = Entradas