from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Book,Author,BookInstance,Genre,Language
from django.views.generic import CreateView,DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .forms import AuthorForm, InstanceForm



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

class GenreCreate(LoginRequiredMixin, CreateView):
    model=Genre
    fields='__all__'

def BookDetail(request,pk):
    #book = Book.objects.filter(pk=primary_key)
    book=get_object_or_404(Book, pk=pk)
    return render(request,'catalog/book_detail.html',context={'book':book})

def ListBookDetails(request):
    all_books=Book.objects.all()
    for abook in all_books:
        abook.num_inst=BookInstance.objects.filter(book=abook.id).count()
    return render(request,'catalog/list_books_detail.html',context={'books':all_books})
    
class BookCreate(LoginRequiredMixin, CreateView):
    model=Book
    fields='__all__'

class BookUpdate(LoginRequiredMixin, UpdateView):
    model=Book
    fields='__all__'

class BookDelete(LoginRequiredMixin, DeleteView):
    model=Book
    fields='__all__'
    template_name = 'catalog/confirm_delete.html'
    success_url = reverse_lazy('list_books')

class InstanceCreate(LoginRequiredMixin, CreateView):
    model=BookInstance
    form_class=InstanceForm
    template_name='catalog/instance_form.html'
    #print("I am here!")
    def load_title(request):
        book_id=request.GET.get(book_id)
        print(f"the book id is {book_id}")
        pass
        return render(request,'instance_form.html',{'book_id':book_id})
    def get_context_data(self,**kwargs):
        book_id = self.kwargs['book_id']
        if book_id:
            data = super().get_context_data(**kwargs)
            data['book_id']=book_id
            data['form']=InstanceForm(initial={'book':book_id})
            return data
        else:
            data['book_id']="This aint no Chicago!"
            return data

class ListInstances(LoginRequiredMixin, ListView):
    model=Book
    template_name='catalog/list_instance_details.html'
    fields='__all__'
    context_object_name = 'my_objects'
    def get_queryset(self):
        my_id = self.kwargs['pk']
        #return BookInstance.objects.filter(book=my_id)
        return BookInstance.objects.filter(book=my_id)
    def get_context_data(self,**kwargs):
        my_id = self.kwargs['pk']
        data = super().get_context_data(**kwargs)
        data['book_id']=my_id
        return data
    
class AuthorCreate(LoginRequiredMixin, CreateView):
    model=Author
    form_class = AuthorForm

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model=Author
    form_class = AuthorForm

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model=Author
    template_name = 'catalog/confirm_delete.html'
    fields='__all__'
    success_url = reverse_lazy('list_authors')

class AllAuthors(ListView):
    model=Author
    template_name='catalog/list_author.html'
    paginate_by=25
    def get_queryset(self):
        return Author.objects.all()

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
    
# class AllBooks(ListView):
#     model=Book
#     template_name='catalog/list_books.html'
#     paginate_by=25
    
#     def get_queryset(self):
#         return Book.objects.all()
    
