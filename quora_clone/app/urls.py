from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_question_view, name='ask'),
    path('question/<int:question_id>/', views.question_detail_view, name='question_detail'),
    path('question/<int:question_id>/answer/', views.submit_answer_view, name='submit_answer'),
    path('answer/<int:answer_id>/like/', views.like_answer_view, name='like_answer'),
]
