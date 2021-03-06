from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=30)
    image = CloudinaryField("Picture", blank=True, null=True)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=None, null=True)
    likes = models.ManyToManyField(UserModel, related_name='article_likes')

    class ArticleTypes(models.TextChoices):
        sports = 'sports'
        news = 'news'
        activities = 'activities'
        projects = 'projects'
        internships = 'internships'

    category = models.CharField(
        max_length=15,
        choices=ArticleTypes.choices,
        default=ArticleTypes.news,
        )

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return self.comment_set.count()

    @property
    def short_description(self):
        max_words = 30
        split = self.description.split(' ', max_words)
        try:
            split.pop(max_words)
        except IndexError:
            pass
        short_description = ""
        for word in split:
            short_description += word + " "
        short_description = short_description[:-1] + "..."
        self.description = short_description
        return short_description
