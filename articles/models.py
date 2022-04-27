from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):

    title = models.CharField(verbose_name='post title',max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    news = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()


    def get_absolute_url(self):
        return reverse('detail',args = (self.slug,))


    def __str__(self):
        return self.title

class Comment(models.Model):

    description = models.TextField()
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    commented_on = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.description[:10]
