from django.db import models
from .consts import MAX_RATE

CATEGORY = (("work out", "ワークアウト"),("study", "勉強"),("other", "その他"))

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
    )

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True) # 画像用
    video = models.FileField(upload_to='videos/', blank=True, null=True) # 動画用 ★追加
    created_at = models.DateTimeField(auto_now_add=True)