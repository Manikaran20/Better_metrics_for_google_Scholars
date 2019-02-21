# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView

from django.http import HttpResponse

from google_Scholar.forms import IndexForm

from google_Scholar.scrap import Scraper


class IndexView(TemplateView):
	template_name = 'google_Scholar/index.html'

	def get(self, request):
		form = IndexForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = IndexForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['scholar_url']
			scholar_data = Scraper(text)
			b= scholar_data.f
			args = {'b': b}
			return render(request, 'google_Scholar/metrics.html', args)

