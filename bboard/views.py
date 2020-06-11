from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bd, Rubric
from .forms import BbForm

def index(request):
	bbs = Bd.objects.order_by("-published")
	rubrics = Rubric.objects.all()
	context = {"bbs": bbs, "rubrics": rubrics}
	return render(request, 'bboard/index.html', context)	

def by_rubric(request, rubric_id):
	bbs = Bd.objects.filter(rubric=rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(id=rubric_id)

	context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': 'current_rubric'}

	return render(request, 'bboard/by_rubric.html', context)

class BbCreateViews(CreateView):
	template_name = "bboard/create.html"
	form_class = BbForm
	success_url = reverse_lazy("index")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["rubrics"] = Rubric.objects.all()
		return context