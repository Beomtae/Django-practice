from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .forms import PostBaseForm, PostCreateForm

from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    #post_list = Post.objects.filter(writer=request.user)
    context = {
        'post_list':post_list
    }
    return render(request, 'index.html',context)

def post_list_view(request):
    #post_list = Post.objects.all()
    post_list = Post.objects.filter(writer = request.user)
    context ={
        'post_list': post_list
    }
    return render(request, 'posts/post_list.html', context)

@login_required
def post_create_view(request):
    if request.method =='GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content = content,
            writer=request.user
        )
        return redirect('index')

def post_create_form_view(request):
    if request.method =='GET':
        form = PostCreateForm()
        context = {'form':form}
        return render(request, 'posts/post_form2.html',context)
    else:
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid(): #유효성 검사 true
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user,
            )
        else: #유효성 검사 false
            print("유효성 검사 실패")
            return redirect('posts:post-create')
        return redirect('index')

def post_update_view(request,id):
    post = Post.objects.get(id=id)
    if request.method =='GET':
        context = {
            'post':post
        }
        return render(request, 'posts/post_form.html',context)
    elif request.method =='POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        if new_image:
            post.image.delete()
            post.image = new_image
        post.content = content
        post.save()
        return redirect('post_detail',post.id)

def post_detail_view(request, id):
    if request.user.is_authenticated: 
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return redirect('index')
        context = {
            'post':post
        }
        return render(request, 'posts/post_detail.html',context)
    else:
        return redirect('accounts:login')

@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='GET':
        context={
            'post':post
        }
        return render(request,'posts/post_confirm_delete.html',context)
    else:
        post.delete()
        return redirect('index')

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