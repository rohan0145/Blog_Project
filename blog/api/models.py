from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    name=models.CharField(max_length=10,default=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
class Like(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Likes = models.IntegerField(default=True)
    owner = models.ForeignKey('auth.User', related_name='Like', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='Like', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']