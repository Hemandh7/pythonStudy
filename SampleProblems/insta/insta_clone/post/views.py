from django.shortcuts import render

from django.http import JsonResponse
from .models import Post

def create_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        captions = request.POST.get('captions')
        post = Post.objects.create(username=username,captions=captions)
        return render(request,'post/create_post.html')
    return JsonResponse({'message':"INVALID POST"})


def view_posts(request):
    posts=Post.objects.all()
    data=[{'username':post.username, 'captions':post.captions}]
    return render(request,'post/view_posts.html')
    return JsonResponse(data)

def delete_post(request,post_id):
    try:
        post=Post.objects.get(pk=post_id)
        post.delete()
        return JsonResponse({'message':'Post deleted'})
    except Post.DoesNotExist:
        return JsonResponse({'message':"Not Found"})