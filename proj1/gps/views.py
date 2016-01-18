from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gps.models import Post, Post_President

# Create your views here.

def map(request):
    # get all the posts
	if request.method == 'POST':
		Name = request.POST.get('Name')
		Title = request.POST.get('Title')
		X = request.POST.get('Xpos')
		Y = request.POST.get('Ypos')
		Post.objects.create(name=Name,title=Title,Xpos=X,Ypos=Y)
		post_list = Post.objects.all()
		return render_to_response('map.html',
                            {'status': HttpResponse(status=200) , 'post_list': post_list})
	else :
		post_list = Post.objects.all()
		return render_to_response('map.html',
                            {'status': HttpResponse(status=200) , 'post_list': post_list})
	return render_to_response('map.html',
                        {'status': HttpResponse(status=404)})

def president_message(request):
	if request.method == 'POST':
		Name = request.POST.get('Name')
		Title = request.POST.get('Title')
		X = request.POST.get('Xpos')
		Y = request.POST.get('Ypos')
		Post_President.objects.create(name=Name,title=Title,Xpos=X,Ypos=Y)
		post_message = Post_President.objects.all()
		return render_to_response('president_message.html',
                            {'status': HttpResponse(status=200) , 'post_message': post_message})
	else :
		post_message = Post_President.objects.all()
		return render_to_response('president_message.html',
                            {'status': HttpResponse(status=200) , 'post_message': post_message})
	return render_to_response('president_message.html',
                        {'status': HttpResponse(status=404)})
			
def president(request):
	post_message = Post_President.objects.all()
	return render(request,
                  'president.html', {'post_message': post_message})

def locat(request):
	post_list = Post.objects.all()
	return render(request,
                  'locat.html', {'post_list': post_list})
				  
def received(request):
	if request.method == 'POST':
		Name = request.POST.get('Name')
		Title = request.POST.get('Title')
		X = request.POST.get('Xpos')
		Y = request.POST.get('Ypos')
		Post.objects.create(name=Name,title=Title,Xpos=X,Ypos=Y)
		return render_to_response('received.html',
                                  {'status': HttpResponse(status=200) , 'Name' : Name,'Title' : Title , 'Xpos' : X , 'Ypos' : Y})
	return render_to_response('received.html',
                              {'status': HttpResponse(status=404)})

