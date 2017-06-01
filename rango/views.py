from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

#def index(request):
	#return HttpResponse("Let us now go to about page <a href='/rango/about'<br>about</a>")

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return HttpResponse("I'm done..let us go back <br> <a href='/rango'> back</a>")


# Create your views here.
