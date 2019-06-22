from django.contrib.sitemaps import Sitemap
from article.models import Article


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

