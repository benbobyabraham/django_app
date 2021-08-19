from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post 
from .forms import PostForm


# Create your views here.
def index(request):
	#If the method is POST
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES)
		img = PostForm(request.FILES)
		#If the form is valid
		if form.is_valid():
			#Yes, Save
			print('step1')
			form.save()

			#Redirect to Home
			return HttpResponseRedirect("/")
		else:
			#No, Show Error
			print('step2')
			return HttpResponseRedirect(form.errors.as_json())
	else :
		form = PostForm()
		print('step3')

	print('step4')
	# Get all posts , limit = 20
	posts = Post.objects.all()[:20]

	# Show
	print('step  5')
	return render(request, 'posts.html', {'posts':posts,'form':form})

def delete(request, post_id):
	#Find post
	post = Post.objects.get(id = post_id)
	post.delete()
	output = 'POST ID is ' + str(post_id)
	return HttpResponseRedirect('/')
