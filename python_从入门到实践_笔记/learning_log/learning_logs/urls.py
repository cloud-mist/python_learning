'''定义learning_logs 的URL模式'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #主页
    path('', views.index, name='index'),
    
    #显示所有主题
    path('topics/', views.topics, name='topics'),

    #特定主题详细页面   使用主题的id
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic')
]