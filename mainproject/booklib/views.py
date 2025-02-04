from django.shortcuts import render , redirect ,get_object_or_404
from .models import Book
from .forms import AddBookForm , UpdateBookForm , AddReviewForm

def home (request):
   allBooks=Book.objects.all()
   return render(request , 'home.html' ,context={'allBooks':allBooks})

def bookdetail(request , bookid):
    book = Book.objects.get(id=bookid)
    reviews=book.reviews.all()
    return render(request,'detail.html' , {'book':book , 'reviews': reviews})

def delete(request,bookid):
    Book.objects.get(id=bookid).delete()
    return redirect('home')  
def addbook(request):
        if request.method == 'POST':
            form = AddBookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = AddBookForm()
        return render (request ,'addbook.html' , {'form':form}) 
def update(request,bookid):
    todo=Book.objects.get(id=bookid)
    if request.method=='POST':
        form=UpdateBookForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('bookdetail' , bookid )
    else:
        form = UpdateBookForm(instance=todo)
    return render(request , 'update.html' , {'form':form})

def addreview(request, bookid):
    book = get_object_or_404(Book, id=bookid)
    
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book  # اتصال نظر به کتاب
            review.save()
            return redirect("bookdetail", bookid=book.id)  # هدایت به صفحه جزئیات کتاب

    else:
        form = AddReviewForm()

    return render(request, "addreview.html", {"form": form, "book": book})