from django.db import models
from django.conf import settings
       
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-creation_date']
        
    def __str__(self):
        return str(self.title)

class PostLikes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=False,related_name='post_like')
    creation_date = models.DateTimeField(auto_now_add=True)
