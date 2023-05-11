from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request):
    return render(request, 'posts/post_form.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

def url_view(request):
    print('url_view()')
    data = {'code':'001', 'msg':'OK'}
    return HttpResponse('url_view')
    # return JsonResponse(data)

def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(f'username: {username}') # 변수로 값 받기
    print(f'request.GET: {request.GET}') #파라미터로 값 받기
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method =='GET':
        print(f'request.GET: {request.GET}')
    elif request.method=='POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'