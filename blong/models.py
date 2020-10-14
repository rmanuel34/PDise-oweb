from django.db import models
from django.contrib.auth.models import User

import uuid


class Categoria(models.Model):
	descripcion = models.CharField(max_length=60,
							 		help_text='Descripcion de la categoria')
	autor = models.ForeignKey(User,
									on_delete=models.PROTECT,
									help_text='selecione el autor de la categoria')
	def __str__(self):
		return self.descripcion

class Publicacion(models.Model):
	id = models.UUIDField(primary_key= True, editable=False,  default=uuid.uuid4)
	titulo = models.CharField(max_length=200,
											help_text='escriba el titulo de la Publicacion')
	contenido = models.TextField(max_length=20000,
											help_text='escriba el contenido de la Publicacion')
	autor = models.ForeignKey(User,
								on_delete=models.PROTECT,
								help_text='seleccione el autor de la categoria')
	f_pub = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicacion')
	categorias = models.ManyToManyField(Categoria,
										help_text='selccione las categorias')
	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Publicacion'
		verbose_name_plural = 'Publicaciones'
		ordering = ['-f_pub']

