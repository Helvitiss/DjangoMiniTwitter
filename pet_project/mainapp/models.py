from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()


# Модель для постов
class Post(models.Model):
    content = models.TextField(blank=False, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='like_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Post {self.id}'

    class Meta:
        ordering = ['-created_at']



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} commented on {self.post.id}"


    class Meta:
        ordering = ['-created_at']