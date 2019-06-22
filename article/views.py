from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from . import forms
from .models import Article, Comment, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword})
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    categories = Category.objects.all()
    comments = Comment.objects.all()
    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    comments_5 = paginator.get_page(page)
    context = {
        "contacts": contacts,
        "categories": categories,
        "comments": comments_5,
        "articles": articles
    }
    return render(request, "index.html", context)

def about(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword})
    return render(request, "about.html")

def categories(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword})
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        "articles": articles,
        "categories": categories
    }
    return render(request, "categories.html", context)

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = forms.ArticleForm(request.POST or None,request.FILES or None)

    context = {
        "form": form
    }

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.seo = article.title.replace(" ", "-")
        article.seo = article.seo.replace("ı", "i")
        article.seo = article.seo.replace("ğ", "g")
        article.seo = article.seo.replace("Ğ", "G")
        article.seo = article.seo.replace("ü", "u")
        article.seo = article.seo.replace("Ü", "U")
        article.seo = article.seo.replace("Ş", "S")
        article.seo = article.seo.replace("ş", "s")
        article.seo = article.seo.replace("İ", "I")
        article.seo = article.seo.replace("Ö", "O")
        article.seo = article.seo.replace("ö", "o")
        article.seo = article.seo.replace("Ç", "C")
        article.seo = article.seo.replace("ç", "c")
        article.seo = article.seo.replace(",", "")
        list = article.content.split(" ")
        article.read = int(((len(list)) / 200) + 1)
        article.views = 0
        article.save()

        messages.success(request, "Yazı kaydedildi!")
        return redirect("/articles/dashboard")

    return render(request, "addarticle.html", context)

def details(request, slug, title):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword})
    list = (Category.objects.all())
    for i in list:
        k = i.slug
        if slug == str(k):
            article = get_object_or_404(Article, seo = title, category = i)
            comments = article.comments.all()
            context = {
                "article": article,
                "comments": comments
            }
            article.views = article.views + 1
            article.save()
            return render(request, "detail.html", context)
    article.views = article.views + 1
    article.save()
    return render(request, "detail.html", context)

@login_required(login_url = "user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id = id)
    form = forms.ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Yazı güncellendi!")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})

@login_required(login_url = "user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.success(request, "Yazı silindi!")
    return redirect("article:dashboard")

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword})
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, "articles.html", {"contacts": contacts})

def show_category(request, slug):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        categoryList = Category.objects.all()
        return render(request, "articles.html", {"contacts": contacts, "keyword": keyword, "categoryList": categoryList})
    list = (Category.objects.all())
    for i in list:
        k = i.slug
        if slug == str(k):
            articles = Article.objects.filter(category = i)
            paginator = Paginator(articles, 5)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            categoryList = Category.objects.all()
            context = {
                "contacts": contacts,
                "categoryName": i,
                "categoryList": categoryList,
            }
            return render(request, "category.html", context)

    return render(request, "index.html")

def addComment(request, id):
    article = get_object_or_404(Article, id = id)
    slug = article.category.slug
    title = article.seo
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_context = request.POST.get("comment_context")

        newComment = Comment(comment_author = comment_author, comment_content = comment_context)
        newComment.article = article
        newComment.save()

    return redirect("/" + str(slug) + "/" + str(title) + "/")
