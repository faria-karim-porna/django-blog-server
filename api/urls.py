from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('post-list/', views.postList, name="post-list"),
	path('post-detail/<str:pk>/', views.postDetail, name="post-detail"),
	path('post-create/', views.postCreate, name="post-create"),
	path('post-delete/<str:pk>/', views.postDelete, name="post-delete"),

	path('comment-list/', views.commentList, name="comment-list"),
	path('comment-detail/<str:pk>/', views.commentDetail, name="comment-detail"),
	path('comment-detail-by-post/<str:pk>/', views.commentDetailByPost, name="comment-detail-by-post"),
	path('comment-create/', views.commentCreate, name="comment-create"),
	path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete"),
	
	path('vote-list/', views.voteList, name="vote-list"),
	path('vote-detail/<str:pk>/', views.voteDetail, name="vote-detail"),
	path('vote-create/', views.voteCreate, name="vote-create"),
	path('vote-update/<str:pk>/', views.voteUpdate, name="vote-update"),
	path('vote-detail-by-post-and-email/<str:pk>/<str:ek>', views.voteDetailByPostAndEmail, name="vote-detail-by-post-and-email"),
	path('vote-detail-by-post-up/<str:pk>/', views.voteDetailByPostUp, name="vote-detail-by-post-up"),
	path('vote-detail-by-post-down/<str:pk>/', views.voteDetailByPostDown, name="vote-detail-by-post-down"),
	path('vote-delete/<str:pk>/', views.voteDelete, name="vote-delete"),
]
