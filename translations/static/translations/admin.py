from django.contrib import admin
from .models import Project, Chapter, Translator, Editor, Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    # automatically use logged in user to django admin as author to post
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Project)
admin.site.register(Chapter)
admin.site.register(Translator)
admin.site.register(Editor)
admin.site.register(Post, PostModelAdmin)