from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
	Document_date = models.DateTimeField('Дата документа')
	Document_number = models.CharField('Номер', max_length = 15)
	Document_author = models.CharField('Автор', max_length = 40)
	Document_viewmovement = models.CharField('Вид движения', max_length = 20)
	Document_comment = models.CharField('Комментарий', max_length = 40)
	Owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.Document_number

	class Meta:
		verbose_name = 'Документ'
		verbose_name_plural = 'Документы'

class TableProducts(models.Model):
	Document = models.ForeignKey(Document, on_delete = models.CASCADE)
	TableProducts_nomenclature = models.CharField('Номенклатура', max_length = 40)
	TableProducts_quantity = models.CharField('Количество', max_length = 15)
	TableProducts_price = models.CharField('Цена', max_length = 15)
	TableProducts_sum = models.CharField('Сумма', max_length = 15)

	def __str__(self):
		return self.TableProducts_nomenclature

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукция'