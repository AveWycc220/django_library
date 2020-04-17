from django.db import models
from django.shortcuts import reverse
class Input_Book(models.Model):
    title = models.CharField(db_index=True, max_length=150)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title}'
        