# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Quran
from django.http import HttpResponse

# Create your views here.
def beranda(request):	
	quranall = ""
	query = request.GET.get("q")	
	if query:
		quranall = Quran.objects.filter(nama__icontains=query)
		
	return render(request, 'utama/beranda.html', {
			'quranall' : quranall
		})

def quran(request):
	quranall = Quran.objects.all()
	
	query = request.GET.get("q")	
	if query:
		quranall = quranall.filter(nama__icontains=query)

	return render(request, 'utama/quran.html', {
			'quranall' : quranall
		})

def arrayyan(request):
	arrayyan = Quran.objects.filter(nama__icontains="rayyan")
	quranall = Quran.objects.all()
	query = request.GET.get("q")
	if query:
		arrayyan = quranall.filter(nama__icontains=query)

	return render(request, 'utama/arrayyan.html', {
			'arrayyan' : arrayyan
		})

def fasya(request):
	fasya = Quran.objects.filter(nama__icontains="fasya")
	quranall = Quran.objects.all()	
	query = request.GET.get("q")
	if query:
		fasya = quranall.filter(nama__icontains=query)
		
	return render(request, 'utama/fasya.html', {
			'fasya' : fasya			
		})

def pembelian(request):
	return render(request, 'utama/pembelian.html')

def form_action(request):

	alamat = request.POST.post('alamat')
	print alamat