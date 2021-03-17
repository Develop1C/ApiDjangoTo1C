from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Document, TableProducts 
from .forms import DocumentForm, TableProductsForm

# Create your views here.

#def index(request):
#    return render(request, 'apidocuments/list.html')

def documents(request):
	documents = Document.objects.order_by()
	context = {'documents': documents}
	return render(request, 'apidocuments/documents.html', context)

@login_required
def document(request, document_id):
	"""Выводит одну тему и все ее записи."""
	getdocument = Document.objects.get(id=document_id)
	tableproducts = getdocument.tableproducts_set.all()

	context = {'document': getdocument, 'tableproducts': tableproducts}
	return render(request, 'apidocuments/document.html', context)

@login_required
def new_document(request):
	#Создает новый документ
	if request.method != 'POST':
		#Данные не отправлялись, создается пустая форма.
		form = DocumentForm()
	else:
		#Отправлены данные POST; обработать данные.
		form = DocumentForm(data=request.POST)
		if form.is_valid():
			new_document = form.save(commit=False)
			new_document.Owner = request.user
			new_document.Document_author = request.user
			new_document.save()
			return redirect('apidocuments:documents')
	# Вывести пустую или недействтиельную форму.
	context = {'form': form}
	return render(request, 'apidocuments/new_document.html', context)

@login_required
def new_tableproducts(request, document_id):
	document = Document.objects.get(id=document_id)
	if request.method != 'POST':
		form = TableProductsForm()
	else:
		form = TableProductsForm(data=request.POST)
		if form.is_valid():
			new_tableproducts = form.save(commit=False)
			new_tableproducts.Document = document
			new_tableproducts.save()
			return redirect('apidocuments:document', document_id=document_id)
	context = {'document' : document, 'form': form}
	return render(request, 'apidocuments/new_tableproducts.html', context)

@login_required
def edit_tableproducts(request, tableproducts_id):
	tableproducts = TableProducts.objects.get(id=tableproducts_id)
	document = tableproducts.Document

	if request.method != 'POST':
		form = TableProductsForm(instance=tableproducts)
	else:
		form = TableProductsForm(instance=tableproducts, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('apidocuments:document', document_id=document.id)
	context = {'tableproducts' : tableproducts, 'document': document, 'form': form}
	return render(request, 'apidocuments/edit_tableproducts.html', context)