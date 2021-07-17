from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.template.defaultfilters import slugify
import romkan

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=105)
    content = models.TextField(max_length=1000)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    tags = ManyToManyField(Tag)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(romkan.to_roma(self.title))
        super(Post, self).save(*args, **kwargs)