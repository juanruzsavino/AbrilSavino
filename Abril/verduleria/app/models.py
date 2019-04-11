# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models




class Producto(models.Model):
	nombre = models.CharField(max_length=142)
	precio = models.IntegerField()


	def __str__(self):
		return 'Producto {}'.format(self.nombre)    


class Cliente(models.Model):
	nombre = models.CharField(max_length=142)


	def __str__(self):
		return 'Cliente {}'.format(self.nombre)


class Factura(models.Model):
	fecha_de_factura = models.DateTimeField(editable=True)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)