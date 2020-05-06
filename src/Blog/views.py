from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Article
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

from .forms import ArticleForm
# Create your views here.

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	# success_url = '/'
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article,id = id_)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	# success_url = '/'
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)
	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article,id = id_)	

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	queryset = Article.objects.all()
	# success_url = "../../"
	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article,id = id_)
	
	def get_success_url(self):
		return reverse('articles:article-list')