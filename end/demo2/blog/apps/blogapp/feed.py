# Charlie
# date:2020/2/21 16:00
# file_name:feed
from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class ArticleFeed(Feed):
    title = 'WED全栈开发技术'
    description = '定期发布一系列Web开发技术'
    link = '/'

    def items(self):
        return Article.objects.all().order_by('-create_time')[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        url = reverse('blogapp:detail', args=(item.id,))
        return url
