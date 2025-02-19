from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book,Author,BookInstance,Genre,Language
from django.views.generic import CreateView,DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    num_book=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_avail=BookInstance.objects.filter(status__exact='a').count()
    context={
        'books':num_book,
        'inst':num_instances,
        'avail':num_instances_avail
        }

    return render(request,'catalog/index.html',context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model=Book
    fields='__all__'

class AuthorCreate(LoginRequiredMixin, CreateView):
    model=Author
    fields='__all__'

#class BookDetail(DetailView):
#    model=Book
#    inst=model.title
#    def get_context_data(self, **kwargs):
#        context =super().get_context_data(**kwargs)
#        #context['inst']=self.inst
#        context['test']="Hello Tom"
#        return context

def BookDetail(request,pk):
    #book = Book.objects.filter(pk=primary_key)
    book=get_object_or_404(Book, pk=pk)
    return render(request,'catalog/book_detail.html',context={'book':book})

@login_required
def my_view(request):
    return render(request,'catalog/my_view.html')

class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url = reverse_lazy('login')
    template_name='catalog/signup.html'

class CheckedOutBooksByUser(LoginRequiredMixin,ListView):
    #list all bookinstance filtered by user session
    model=BookInstance
    template_name='catalog/profile.html'
    paginate_by=5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()
    
class AllBooks(ListView):
    model=Book
    template_name='catalog/list_books.html'
    paginate_by=5

    def get_queryset(self):
        return Book.objects.all()