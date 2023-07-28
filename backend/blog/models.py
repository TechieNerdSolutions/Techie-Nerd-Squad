from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import now
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.html import mark_safe
from author.models import Author
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    table_of_contents = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(Author)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    comments_enabled = models.BooleanField(default=True)
    likes_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' | ' + ', '.join(str(author) for author in self.authors.all())


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class PostStatusHistory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='status_history')
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    date_updated = models.DateTimeField(default=now)

    def __str__(self):
        return f"Post {self.post.title} changed status to {self.status} on {self.date_updated}"

class PostExcerpt(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='excerpt')
    excerpt = models.TextField()

    def __str__(self):
        return f"Excerpt for {self.post.title}"

class RelatedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='related_posts')
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Related post '{self.related_post.title}' for post '{self.post.title}'"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} for post '{self.post.title}'"

class ReadTime(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='read_time')
    minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"Read time for post '{self.post.title}': {self.minutes} minutes"

class SocialMediaSharing(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='social_media_sharing')
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f"Social media sharing for post '{self.post.title}'"