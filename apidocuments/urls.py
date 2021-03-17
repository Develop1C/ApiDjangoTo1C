from django.urls import path
from . import views

app_name = 'apidocuments'

urlpatterns = [
	path('', views.documents, name= 'documents'),
	path('documents/', views.documents, name='documents'),
	path('<int:document_id>/', views.document, name= 'document'),
	path('new_document/', views.new_document, name= 'new_document'),
	path('new_tableproducts/<int:document_id>/', views.new_tableproducts, name= 'new_tableproducts'),
	path('edit_tableproducts/<int:tableproducts_id>/', views.edit_tableproducts, name='edit_tableproducts')
]