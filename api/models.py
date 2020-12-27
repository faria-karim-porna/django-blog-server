from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=200)
  category = models.CharField(max_length=200)
  body = models.TextField()
  author_name = models.CharField(max_length=200)
  author_email = models.CharField(max_length=200)
  author_image = models.CharField(max_length=200)
  post_date = models.DateField(auto_now_add= True)

class Comment(models.Model):
  post_id = models.CharField(max_length=200)
  comment = models.TextField()
  commentor_name = models.CharField(max_length=200)
  commentor_email = models.CharField(max_length=200)
  commentor_image = models.CharField(max_length=200)
  comment_date = models.DateField(auto_now_add= True)

class Vote(models.Model):
  post_id = models.CharField(max_length=200)
  voter_email = models.CharField(max_length=200)
  up_vote = models.BooleanField(default=False, blank=True, null=True)
  down_vote = models.BooleanField(default=False, blank=True, null=True)
  up_vote_color = models.CharField(max_length=200)
  down_vote_color = models.CharField(max_length=200)
      
  def __str__(self):
    return self.title