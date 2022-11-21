from django.db import models


class Blog_post(models.Model):
    s_no = models.AutoField(primary_key=True)
    Blog_title = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    article = models.TextField()
    author = models.CharField(max_length=50)
    Slug = models.CharField(max_length=150)
    author_image = models.ImageField(
        upload_to='author_image', null=True, default=None)
    blog_image = models.ImageField(
        upload_to='blog_image', null=True, default=None)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return 'Blog from '+self.author
