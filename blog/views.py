from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'AlexFeld',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'July 21, 2020'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'July 22, 2020'
	}

]

def home(request):
	# return HttpResponse('<h1> Blog Home </h1>')
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	# return HttpResponse('<h1> Blog About </h1>')
	return render(request, 'blog/about.html', {'title': 'About'})
