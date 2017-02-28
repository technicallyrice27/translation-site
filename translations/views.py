from django.shortcuts import render, get_object_or_404, redirect
from .models import Chapter, Project, Post
# Create your views here.
from django.http import HttpResponse

def home(request):
    latest_news = Post.objects.latest('posted_date')
    projects = Project.objects.all().order_by('title')
    latest_chapters = [Chapter.objects.filter(project__pk=project.pk).order_by('-number')[0] for project in projects]
    return render(request, 'translations/home.html', {'latest_news': latest_news, 'latest_chapters': latest_chapters, 'projects': projects})

def projects(request):
    projects = Project.objects.all().order_by('title')
    return render(request, 'translations/projects.html', {'projects': projects})

def project_page(request, pt):
    project = get_object_or_404(Project, slug__iexact=pt)
    chapters = Chapter.objects.filter(project__pk=project.pk).filter(complete=True).order_by('number')
    return render(request, 'translations/project_page.html', {'project': project, 'chapters': chapters})

def table_of_contents_old(request, ppk):
    project = get_object_or_404(Project, pk=ppk)
    return redirect('project_page', pt=project.slug, permanent=True)

def chapter_display_old(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return redirect('chapter_display', pt=chapter.project.slug, num=chapter.number, permanent=True)

def chapter_display(request, pt, num):
    chapter = get_object_or_404(Chapter, number=num, project__slug__iexact=pt)
    current_chapter = chapter.number
    project = chapter.project.slug
    try:
        prevch = Chapter.objects.get(number__exact=current_chapter-1, project__slug__exact=project)
    except Chapter.DoesNotExist:
        prevch = None
    try:
        nextch = Chapter.objects.get(number__exact=current_chapter+1, project__slug__exact=project)
    except Chapter.DoesNotExist:
        nextch = None
    if nextch is not None and nextch.complete == False:
        nextch = None
    return render(request, 'translations/chapter_display.html', {'chapter': chapter, 'prevch': prevch, 'nextch': nextch})

def news(request):
    posts = Post.objects.all().order_by('-posted_date')
    return render(request, 'translations/news.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'translations/post.html', {'post': post})

def post_old(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return redirect('post', slug=post.slug, permanent=True)

def contact(request):
    return render(request, 'translations/contact.html')