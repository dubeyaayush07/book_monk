from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( 
    ListView, 
    DetailView, 
    CreateView,
    UpdateView, 
    DeleteView
)
from django.contrib.auth.models import User
from .models import Book

# Create your views here.

def about(request):
    return render(request, 'books/about.html')

class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'book_set'
    ordering = ['-date_posted']
    paginate_by = 5

class UserBookListView(ListView):
    model = Book
    template_name = 'books/user_books.html'
    context_object_name = 'book_set'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(post_author=user).order_by('-date_posted')

class BookDetailView(DetailView):
    model = Book
  

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'details', 'for_rent', 'for_sale', 'contact_info']

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)



class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'details', 'for_rent', 'for_sale', 'contact_info']

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.post_author:
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.post_author:
            return True
        return False