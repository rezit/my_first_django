# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quran(models.Model):
	nama = models.CharField(max_length = 200)
	# berat = models.PositiveIntegerField(null=True, blank=True)
	harga = models.PositiveIntegerField(null=True, blank=True)
	kode = models.CharField(max_length = 200)	
	gambar = models.ImageField(null=True, blank=True)

	def __unicode__(self):
		return self.nama

class Buku(models.Model):
	judul = models.CharField(max_length = 200)
	penulis = models.CharField(max_length = 200)
	penerbit = models.CharField(max_length = 200) 
	# harga = PositiveIntegerField(max_length = 20)

	def __unicode__(self):
		return self.judul

class Baju(models.Model):
	nama = models.CharField(max_length = 200)
	# berat = PositiveIntegerField(max_length = 4)
	# harga = PositiveIntegerField(max_length = 20)

	def __unicode__(self):
		return self.nama