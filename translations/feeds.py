# RSS Feed
from django.contrib.syndication.views import Feed
from django.urls import reverse
from translations.models import Chapter

class LatestChapters(Feed):
    title = "OP Translations' Latest Chapter Releases"
    link = "/projects/"
    description = "Updates on new chapters for OP Translations' projects"

    def items(self):
        return Chapter.objects.order_by('-posted_date')[:20]

    def item_title(self, item):
        #title = item.project.title + ' - ' + item.project.jpengtitle + ' - ' + 'Chapter ' + item.number + ' - ' item.title
        title = '{} - {} - Chapter {} - {}'.format(item.project.title, 
        item.project.jpengtitle, item.number, item.title)
        return title
    
    def item_pubdate(self, item):
        return item.posted_date
    
    def item_description(self, item):
        return (item.content[:100] + '...') if len(item.content) > 100 else item.content

    def item_link(self, item):
        return reverse('chapter_display', args=[item.project.slug, item.number])