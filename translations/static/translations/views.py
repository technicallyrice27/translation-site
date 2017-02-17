from django.shortcuts import render, get_object_or_404
from .models import Chapter, Project, Post
# Create your views here.
from django.http import HttpResponse

def home(request):
    projects = Project.objects.all().order_by('title')
    return render(request, 'translations/home.html', {'projects': projects})

def projects(request):
    projects = Project.objects.all().order_by('title')
    return render(request, 'translations/projects.html', {'projects': projects})

def counterstop(request):
    project = Project.objects.get(title__iexact='counter stop!')
    return render(request, 'translations/counterstop.html', {'project': project})

def table_of_contents(request, ppk):
    proj = get_object_or_404(Project, pk=ppk)
    project_title = proj.title
    chapters = Chapter.objects.filter(project__title__iexact=project_title).filter(complete=True).order_by('number')
    return render(request, 'translations/table_of_contents.html', {'chapters': chapters})

def chapter_display(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    current_chapter = chapter.number
    project = chapter.project.title
    try:
        prevch = Chapter.objects.get(number__exact=current_chapter-1, project__title__exact=project)
    except Chapter.DoesNotExist:
        prevch = None
    try:
        nextch = Chapter.objects.get(number__exact=current_chapter+1, project__title__exact=project)
    except Chapter.DoesNotExist:
        nextch = None
    if nextch is not None and nextch.complete == False:
        nextch = None
    return render(request, 'translations/chapter_display.html', {'chapter': chapter, 'prevch': prevch, 'nextch': nextch})

def news(request):
    posts = Post.objects.all().order_by('-posted_date')
    return render(request, 'translations/news.html', {'posts': posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'translations/post.html', {'post': post})

def contact(request):
    return render(request, 'translations/contact.html')