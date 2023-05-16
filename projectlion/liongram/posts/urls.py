from django.urls import path

from .views import post_list_view,post_create_view,post_update_view,post_detail_view,post_delete_view

app_name='posts' #html 에서 url을 name으로 설정할때 필요 posts:post-create 등

urlpatterns=[
    path('', post_list_view, name='post-list'),
    path('new/', post_create_view, name='post-create'),
    path('edit/<int:id>', post_update_view, name='post-update'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('delete/<int:id>', post_delete_view, name="post-delete"),
]