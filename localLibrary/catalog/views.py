from django.shortcuts import render
# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()   # 책의 갯수
    num_instances = BookInstance.objects.all().count()   
    
    # Available books filtering (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    # context_object_name = 'book_list'
    # queryset = Book.objects.all()
    # template_name = 'book_list.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author
