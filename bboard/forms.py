from django.forms import ModelForm

from .models import Bd

class BbForm(ModelForm):
	class Meta:
		model = Bd
		fields = ('title', 'content', 'rubric', 'price')