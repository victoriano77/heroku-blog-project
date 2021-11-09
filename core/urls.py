from django.urls import path

from core.views import home, blogDetail,createBlog, updateBlog, blogDelete

app_name = 'core'

urlpatterns = [
    path('', home.as_view(), name="home"),#class url
    # path('', home, name="home"),
  #  path("createBlog/", createBlog, name="createBlog"),
    path("createBlog/", createBlog.as_view(), name="createBlog"),
    
   # path('<str:pk>/', blogDetail, name="blogDetail"), 
    path('<str:pk>/', blogDetail.as_view(), name="blogDetail"), 
   # path('<str:pk>/update', updateBlog, name="updateBlog"),
     path('<str:pk>/update', updateBlog.as_view(), name="updateBlog"),
    path('<str:pk>/delete', blogDelete, name="delete"),
    

    
]