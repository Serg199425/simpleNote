from django.shortcuts import render
from django.views.generic import TemplateView

class AboutUsView(TemplateView):
	template_name = "content_pages/about_us.html"