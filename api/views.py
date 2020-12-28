from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, VoteSerializer

from .models import Post, Comment, Vote
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Post List':'/post-list/',
		'Post Detail View':'/post-detail/<str:pk>/',
		'Post Create':'/post-create/',
		'Post Delete':'/post-delete/<str:pk>/',

		'Comment List':'/comment-list/',
		'Comment Detail View':'/comment-detail/<str:pk>/',
		'Comment Detail View By Posts':'/comment-detail-by-post/<str:pk>/',
		'Comment Create':'/comment-create/',
		'Comment Delete':'/comment-delete/<str:pk>/',

		'Vote List':'/vote-list/',
		'Vote Detail View':'/vote-detail/<str:pk>/',
		'Vote Create':'/vote-create/',
		'Vote Detail View By Posts and Email':'/vote-detail-by-post-and-email/<str:pk>/<str:ek>/',
		'Vote Detail View By Posts Up':'/vote-detail-by-post-up/<str:pk>/',
		'Vote Detail View By Posts Down':'/vote-detail-by-post-down/<str:pk>/',
		'Vote Update':'/vote-update/<str:pk>/',
		'Vote Delete':'/vote-delete/<str:pk>/',
		}

	return Response(api_urls)
# view posts
@api_view(['GET'])
def postList(request):
	posts = Post.objects.all().order_by('-id')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)
# view single post
@api_view(['GET'])
def postDetail(request, pk):
	posts = Post.objects.get(id=pk)
	serializer = PostSerializer(posts, many=False)
	return Response(serializer.data)

#create posts
@api_view(['POST'])
def postCreate(request):
	serializer = PostSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#delete posts
@api_view(['DELETE'])
def postDelete(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()

	return Response('Item succsesfully delete!')

# comment
# view comments
@api_view(['GET'])
def commentList(request):
	comments = Comment.objects.all().order_by('-id')
	serializer = CommentSerializer(comments, many=True)
	return Response(serializer.data)
#view single comment
@api_view(['GET'])
def commentDetail(request, pk):
	comments = Comment.objects.get(id=pk)
	serializer = CommentSerializer(comments, many=False)
	return Response(serializer.data)
#view all comments of a post
@api_view(['GET'])
def commentDetailByPost(request, pk):
	comments = Comment.objects.filter(post_id=pk)
	serializer = CommentSerializer(comments, many=True)
	return Response(serializer.data)

#create comments
@api_view(['POST'])
def commentCreate(request):
	serializer = CommentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# delete comments
@api_view(['DELETE'])
def commentDelete(request, pk):
	comment = Comment.objects.get(id=pk)
	comment.delete()

	return Response('Item succsesfully delete!')

# vote
# view votes
@api_view(['GET'])
def voteList(request):
	votes = Vote.objects.all().order_by('-id')
	serializer = VoteSerializer(votes, many=True)
	return Response(serializer.data)
# view a single vote
@api_view(['GET'])
def voteDetail(request, pk):
	votes = Vote.objects.get(id=pk)
	serializer = VoteSerializer(votes, many=False)
	return Response(serializer.data)

# create votes
@api_view(['POST'])
def voteCreate(request):
	serializer = VoteSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
# update votes
@api_view(['POST'])
def voteUpdate(request, pk):
	vote = Vote.objects.get(id=pk)
	serializer = VoteSerializer(instance=vote, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
# votes of a post by a person
# will help to show a user of his/her current vote condition 
@api_view(['GET'])
def voteDetailByPostAndEmail(request, pk, ek):
	votes = Vote.objects.filter(post_id=pk).filter(voter_email=ek)
	serializer = VoteSerializer(votes, many=True)
	return Response(serializer.data)
# all up votes
# help to count up votes
@api_view(['GET'])
def voteDetailByPostUp(request, pk):
	votes = Vote.objects.filter(post_id=pk).filter(up_vote=True)
	serializer = VoteSerializer(votes, many=True)
	return Response(serializer.data)
# all down votes
# help to count down votes
@api_view(['GET'])
def voteDetailByPostDown(request, pk):
	votes = Vote.objects.filter(post_id=pk).filter(down_vote=True)
	serializer = VoteSerializer(votes, many=True)
	return Response(serializer.data)
	
# delete votes
@api_view(['DELETE'])
def voteDelete(request, pk):
	vote = Vote.objects.get(id=pk)
	vote.delete()

	return Response('Item succsesfully delete!')