from django.urls import path
from . import views

app_name = 'articles' # 다른 앱에도 detail같이 변수 같은 경우 발생할 수 있어서 정해주는 역할

urlpatterns = [
    path('', views.index, name='index'), # 이 경로를 'index'로 변수화
    path('<int:id>/', views.detail, name='detail'), # `name=`이 인스턴스화 역할 함

]