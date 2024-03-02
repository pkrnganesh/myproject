from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   name = 'patrick'
   return render(request, 'index.html')

def counter(request):
   text = request.GET['text'] # name of the textarea tag iin form
   amount_of_words = len(text.split())
   return render(request, 'counter.html', {'amount': amount_of_words})