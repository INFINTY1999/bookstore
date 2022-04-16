from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Books,Store

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

        
class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['Book_name','Book_price','Numb_books','Author_name']

    def __init__(self, *args, **kwargs):
        super(BooksForm, self ).__init__(*args, **kwargs)

class StoreForm(ModelForm):
    
    class Meta:
        model = Store
        fields = ['store_name','state','Address','Books']

    def __init__(self, *args, **kwargs):
        super(StoreForm, self ).__init__(*args, **kwargs)

class StorebookForm(ModelForm):
    
    class Meta:
        model = Store
        fields = ['Books']

    def __init__(self, *args, **kwargs):
        super(StorebookForm, self ).__init__(*args, **kwargs)