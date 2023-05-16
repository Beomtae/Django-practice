from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from posts.views import class_view, url_view,url_parameter_view,function_view,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<str:username>/',url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view(), name='cbv'),
    
    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
