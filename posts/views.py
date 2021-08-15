from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post 
from .forms import PostForm


# Create your views here.
def index(request):
	#If the method is POST
	if request.method == "POST":
		form = PostForm(request.POST)
		#If the form is valid
		if form.is_valid():
			#Yes, Save
			form.save()

			#Redirect to Home
			return HttpResponseRedirect("/")
		else:
			#No, Show Error
			return HttpResponseRedirect(form.errors.as_json())


	# Get all posts , limit = 20
	posts = Post.objects.all()[:20]

	# Show
	return render(request, 'posts.html', {'posts':posts})

def delete(request, post_id):
	#Find post
	post = Post.objects.get(id = post_id)
	post.delete()
	output = 'POST ID is ' + str(post_id)
	return HttpResponseRedirect('/')
