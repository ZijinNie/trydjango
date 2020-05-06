from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	
	title 		= forms.CharField(widget = forms.TextInput( attrs = {'placeholder': "plz insert title"}))
	
	description = forms.CharField(
									widget = forms.Textarea(
										attrs = {
											'class' : 'new-class-name two',
											'placeholder': "plz insert des",
											'id' : 'id-for-text-area',
											'name' : 'text-area',
											'rows' : 20,
											'cols' : 120
										}									
									))

	price 		= forms.DecimalField(initial = 199)
	class Meta:
		model = Product
		fields = {
			'title',
			'description',
			'price'
		}

	# def clean_title(self):
	# 	title = self.cleaned_data.get('title')
	# 	if 'CFE' in title:
	# 		return title
	# 	else:
	# 		raise forms.ValidationError("This is not a valid title")

class RawProductForm (forms.Form):
	title 		= forms.CharField(widget = forms.TextInput( attrs = {'placeholder': "plz insert title"}))
	description = forms.CharField(	required = False, 
									widget = forms.Textarea(
										attrs = {
											'class' : 'new-class-name two',
											'placeholder': "plz insert des",
											'id' : 'id-for-text-area',
											'name' : 'text-area',
											'rows' : 20,
											'cols' : 120
										}									
									))
	price 		= forms.DecimalField(initial = 199)

