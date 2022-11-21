from django.http import HttpResponse
from django.shortcuts import render
from app.models import Contact, Subscribe, Review
from blog.models import Blog_post
from app.models import Empoly

from django.core.paginator import Paginator

# Create your views here.


def home(request):
    if request.method == 'POST':
        if len(request.POST) == 5:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            contact = Contact(clint_name=name, subject=subject,
                              message=message, clint_email=email)
            contact.save()

        elif len(request.POST) == 2:
            name = request.POST['subscribe']
            cont = Subscribe(s_email=name)
            cont.save()
    allPosts = Blog_post.objects.all()
    paginator = Paginator(allPosts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for empoly
    empPosts = Empoly.objects.all()
    review = Review.objects.all()
    context = {'navbar': 'home', 'allPosts': page_obj,
               'Emp_post': empPosts, 'review': review}
    return render(request, '../templets/index.html', context)


def about(request):
    if request.method == 'POST':
        if len(request.POST) == 2:
            name = request.POST['subscribe']
            cont = Subscribe(s_email=name)
            cont.save()
    empPosts = Empoly.objects.all()
    context = {'navbar': 'about', 'Emp_post': empPosts}
    return render(request, '../templets/about.html', context)


def services(request):
    if request.method == 'POST':
        if len(request.POST) == 2:
            name = request.POST['subscribe']
            cont = Subscribe(s_email=name)
            cont.save()
    review = Review.objects.all()
    return render(request, '../templets/services.html', {'navbar': 'services', 'review': review})


def projects(request):

    if request.method == 'POST':
        if len(request.POST) == 2:
            name = request.POST['subscribe']
            cont = Subscribe(s_email=name)
            cont.save()
    return render(request, '../templets/projects.html', {'navbar': 'projects'})


def contact(request):
    if request.method == 'POST':
        if len(request.POST) == 5:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            contact = Contact(clint_name=name, subject=subject,
                              message=message, clint_email=email)
            contact.save()

        elif len(request.POST) == 2:
            name = request.POST['subscribe']
            cont = Subscribe(s_email=name)
            cont.save()

    return render(request, '../templets/contact.html', {'navbar': 'contact'})
