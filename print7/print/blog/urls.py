from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SaleListView,
    SaleDetailView,
    SaleCreateView,
    SaleUpdateView,
    SaleDeleteView,
    SearchResultsView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:slug>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('sale/new/', SaleCreateView.as_view(), name='sale-create'),
    path('sale/', SaleListView.as_view(), name='sale-list'),
    path('sale/<str:slug>/', SaleDetailView.as_view(), name='sale-detail'),
    path('sale/<str:slug>/update/', SaleUpdateView.as_view(), name='sale-update'),
    path('sale/<str:slug>/delete/', SaleDeleteView.as_view(), name='sale-delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]