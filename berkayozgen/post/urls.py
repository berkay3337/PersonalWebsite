
from django.urls import path
from post import views

app_name = 'post'


urlpatterns = [
    
    path('index/', views.post_index,name='index'),
    path('create/', views.post_create,name='create'),
    path('detail/<slug:slug>', views.post_detail,name='detail'),
    path('update/<slug:slug>', views.post_update,name='update'),
    path('delete/<slug:slug>', views.post_delete,name='delete'),
   
    
]