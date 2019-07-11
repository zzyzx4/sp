from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import User
from django.conf import settings
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Sale
from django.db.models import Q
from django import forms
from .forms import PostCreateForm
from ckeditor.widgets import CKEditorWidget


def home(request):
    search_query = request.GET.get('q')
    if search_query:
        posts_search = Post.objects.filter(title__icontains=search_query)
    else:
        posts_search = Post.objects.all()
    context = {
        'posts': Post.objects.all(),
        'posts_search': posts_search,
    }
    return render(request, 'blog/home.html', context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-publish']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    slug = Post.slug
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-publish')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    model = Post
    # fields = ['title', 'content', 'image', 'category', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})

# объявления ============================================================================================
class SaleListView(ListView):
    model = Sale
    template_name = 'blog/sale-list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'sales'
    ordering = ['-publish']
    paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, email=self.kwargs.get('email'))
    #     return Sale.objects.filter(author=user).order_by('-publish')


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'blog/sale-detail.html'


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    fields = ['product', 'description', 'cost', 'image', 'category', 'tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SaleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sale
    fields = ['product', 'description', 'cost', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sale = self.get_object()
        if self.request.user == sale.author:
            return True
        return False


class SaleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sale
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
