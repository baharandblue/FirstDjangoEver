from django import forms
from .models import Book , Review

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title' , 'author' , 'publication_date') 

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title' , 'author' , 'publication_date') 
        
class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =('content',)
        