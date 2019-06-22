from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    slug2 = models.CharField(max_length = 200, null = True)
    parent = models.ForeignKey('self',blank=True, null=True, on_delete = models.CASCADE, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same 
                                                 #slug 

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent                          

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return '/'.join(full_path[::-1])

    def get_absolute_url(self):
        url = "/" + self.slug
        return url


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Yazar")
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")
    created_date = models.DateField(auto_now_add= True, verbose_name = "Tarih")
    article_image = models.FileField(blank = True, null = True, verbose_name = "Resim Ekle")
    seo = models.CharField(max_length = 100, verbose_name = "Seo", null = True)
    read = models.CharField(max_length = 50, verbose_name = "Read", null = True)
    views = models.IntegerField(verbose_name = "View", null = True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-id']

    def get_absolute_url(self):
        url = "/" + self.category.slug + "/" + self.seo
        return url

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Yazı", related_name= "comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200, verbose_name = "Yorum")
    created_date = models.DateTimeField(auto_now_add= True, verbose_name = "Tarih")
    def __str__(self):
        return self.comment_content
    class Meta():
        ordering = ['-created_date']
