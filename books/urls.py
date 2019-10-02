from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView, 
    UserBookListView
)
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='books-home'),
    path('user/<str:username>/', UserBookListView.as_view(), name='user-books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('about/', views.about, name='about'), 

]