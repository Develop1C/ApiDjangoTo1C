from django import forms
from .models import Document, TableProducts

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ['Document_date', 'Document_number', 'Document_viewmovement', 'Document_comment']
		#labels = {'Document_comment': '', 'Document_author': ''}

class TableProductsForm(forms.ModelForm):
	class Meta:
		model = TableProducts
		fields = ['TableProducts_nomenclature', 'TableProducts_quantity', 'TableProducts_price', 'TableProducts_sum']
		#labels = {'TableProducts_nomenclature': 'TableProductsForm:'}
		#widgets = {'text': forms.Textarea(attrs={'cols': 80"})}