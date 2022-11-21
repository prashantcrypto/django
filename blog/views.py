from django.shortcuts import render
from blog.models import Blog_post
from django.core.paginator import Paginator


def blog(request):
    allPosts = Blog_post.objects.all()
    paginator = Paginator(allPosts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_page = page_obj.paginator.num_pages

    context = {'allPosts': page_obj,
               'navbar': 'blog', 'total_page': total_page, 'page_list': [n+1 for n in range(total_page)]}
    return render(request, '../templets/blog.html',  context)


def component(request, slug):
    allPosts = Blog_post.objects.all()
    paginator = Paginator(allPosts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post = Blog_post.objects.filter(Slug=slug).first()
    context = {'navbar': 'blog', 'post': post, 'allPosts': page_obj}
    return render(request, '../templets/blogcomponent.html', context)


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        query = []

    else:

        allPosts = Blog_post.objects.filter(Blog_title__icontains=query)
        allarticle = Blog_post.objects.filter(article__icontains=query)

        allPosts = allPosts.union(allarticle)

    context = {'allPosts': allPosts, 'navbar': 'blog', }
    return render(request, '../templets/search.html',  context)
