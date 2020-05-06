from django import forms
from .models import Article

class ArticleForm (forms.ModelForm):
	title = forms.CharField()
	content =forms.CharField()
	active = forms.BooleanField()

	class Meta:
		model = Article
		fields = {
			'title',
			'content',
			'active'
		}

