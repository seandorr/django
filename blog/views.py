from django.shortcuts import render

posts = [
	{
		'author': 'Sean Dorr',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 24, 2019'
	},
	
	{
		'author': 'Gemma Enriquez',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 25, 2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	
	
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})