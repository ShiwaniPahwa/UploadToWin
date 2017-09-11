
from django.db import models

#uuid genrates random strings

import uuid

#class for user's details
class User(models.Model):
		email = models.EmailField(default=None)
		name = models.CharField(max_length=120)
		username = models.CharField(max_length=120)
		password = models.CharField(max_length=40)
		created_on = models.DateTimeField(auto_now_add=True)
		updated_on = models.DateTimeField(auto_now=True)


#class for creating session token
class SessionToken(models.Model):
		user = models.ForeignKey(User)
		session_token = models.CharField(max_length=255)
		last_request_on = models.DateTimeField(auto_now=True)
		created_on = models.DateTimeField(auto_now_add=True)
		is_valid = models.BooleanField(default=True)
		def create_token(self):
			self.session_token = uuid.uuid4()

#class for posting
class PostModel(models.Model):
		user = models.ForeignKey(User)
		image = models.FileField(upload_to='user_images')
		image_url = models.CharField(max_length=255)
		caption = models.CharField(max_length=240)
		created_on = models.DateTimeField(auto_now_add=True)
		updated_on = models.DateTimeField(auto_now=True)
		has_liked = False


		@property			#it will show the number of likes
		def like_count(self):
			return len(LikeModel.objects.filter(post=self))

		@property			#it will show the commments
		def comments(self):
			return CommentModel.objects.filter(post=self).order_by('-created_on')

		@property
		def categories(self):
			return CategoryModel.objects.filter(post=self)


#class for liking a post
class LikeModel(models.Model):
		user = models.ForeignKey(User)
		post = models.ForeignKey(PostModel)
		created_on = models.DateTimeField(auto_now_add=True)
		updated_on = models.DateTimeField(auto_now=True)



#class for commenting on post
class CommentModel(models.Model):
		user = models.ForeignKey(User)
		post = models.ForeignKey(PostModel)
		comment_text = models.CharField(max_length=555)
		created_on = models.DateTimeField(auto_now_add=True)
		updated_on = models.DateTimeField(auto_now=True)


class CategoryModel(models.Model):
		post = models.ForeignKey(PostModel)
		category_text = models.CharField(max_length=200)