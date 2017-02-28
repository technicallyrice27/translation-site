from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Translator(models.Model):
    first = models.CharField('First Name', max_length=30)
    last = models.CharField('Last Name', max_length=30)
    persona = models.CharField('Displayed Name', max_length=30)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.persona

# Separated now just in case fields change later on
class Editor(models.Model):
    first = models.CharField('First Name', max_length=30)
    last = models.CharField('Last Name', max_length=30)
    persona = models.CharField('Displayed Name', max_length=30)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.persona

class Project(models.Model):
    title = models.CharField('Translated Title', max_length=100)
    jptitle = models.CharField('Japanese Title', max_length=100)
    jpengtitle = models.CharField('Japanese Title (Romaji)', max_length=100)
    author = models.CharField('Japanese Author', max_length=25)
    summary = models.TextField()
    translators = models.ManyToManyField(Translator, blank=True)
    editors = models.ManyToManyField(Editor, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            # Newly created object without custom slug
            self.slug = slugify(self.title)
            if len(self.slug) > 50:
                self.slug = self.slug[:50]
        # Else normal save
        super().save()

class Chapter(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    number = models.PositiveIntegerField('Chapter Number')
    title = models.CharField('Chapter Title', max_length=200)
    content = models.TextField()
    link = models.URLField('link to source')
    translated_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField('ready to be posted', default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.number == 0:
            return 'Prologue - ' + self.title
        else:
            return 'Chapter ' + str(self.number) + ' - ' + self.title

# For News
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, editable=False)
    text = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, editable=False)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        # if > 50 then cut so it is first 50 of title - unique number + hyphen
        # then add number and hyphen back to string
        if len(unique_slug) > 50:
            unique_slug = unique_slug[:50-(num+1)]
            unique_slug = '{}-{}'.format(unique_slug, num)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = self._get_unique_slug()
        # Else normal save
        super().save()