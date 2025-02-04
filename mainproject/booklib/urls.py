from django.urls import path
from . import views

urlpatterns = [
    path ('' , views.home , name='home'),
    path('bookdetail/<int:bookid>/' , views.bookdetail , name='bookdetail'),
    path("delete/<int:bookid>/", views.delete , name="delete"),
    path("update/<int:bookid>/", views.update , name="update"),
    path("addbook/" , views.addbook , name='addbook'),    
    path("addreview/<int:bookid>/", views.addreview , name="addreview"),
   
]
