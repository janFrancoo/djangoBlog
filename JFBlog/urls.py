from django.contrib import admin
from django.urls import path, include
from article import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from article.models import Article, Category
from django.views.generic import TemplateView

info_dict = {
    'queryset': Article.objects.all(),
    'data_field': 'pub_date',
}

info2_dict = {
    'queryset': Category.objects.all(),
    'data_field': 'pub_date',
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('categories/', views.categories, name = "cats"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
    path('<slug:slug>/', views.show_category, name='category'),
    path('<slug:slug>/<slug:title>/', views.details, name = "details"),
    path('sitemap.xml/', sitemap, {'sitemaps': {'article': GenericSitemap(info_dict, priority=0.8), 'cat': GenericSitemap(info2_dict, priority=0.8)}}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]
