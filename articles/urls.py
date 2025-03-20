from django.urls import path
from . import views

app_name = 'articles' # 다른 앱에도 detail같이 변수 같은 경우 발생할 수 있어서 정해주는 역할

urlpatterns = [
    # Read
    path('', views.index, name='index'), # 이 경로를 'index'로 변수화
    path('<int:id>/', views.detail, name='detail'), # `name=`이 인스턴스화 역할 함

    # Create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # Delete
    path('<int:id>/delete/', views.delete, name='delete'),

    #Update
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
]