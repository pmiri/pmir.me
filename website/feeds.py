from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestEntriesFeed(Feed):
    title = "wtchcrft"
    link = "/rss/"
    description = "shouts into the depths below"

    def items(self):
        return Post.objects.order_by('-created_at')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.post

    def item_link(self, item):
        return reverse('post', args=[item.pk])
