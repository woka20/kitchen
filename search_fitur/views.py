from django.shortcuts import render
from .models import Post, User,Komen
from django.db.models import Q


# Create your views here.
def index(request):
    blog=Post.objects.all()
    komen=Komen.objects.all()
    ctx={"blogs": blog, 'komen':komen}
    return render(request, 'search_fitur/index.html', ctx)

def coba(request, blog_id):
    blog=Post.objects.filter(pk=blog_id)
    komen=Komen.objects.filter(post_id=blog_id)
    ctx={'blog':blog, 'komen':komen}
    return render(request, 'search_fitur/detail.html', ctx )

def kategori(request):
    blog=Post.objects.all().distinct()
    return render(request, "search_fitur/category1.html", {"blogs":blog})

# def display_kategori(request):
#     return render(request, 'search_fitur/category1.html', {})

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(konten__icontains=query)
            new= Q(nama_lengkap__icontains=query)

            results= Post.objects.filter(lookups).distinct()
            user_result=User.objects.filter(new).distinct()

            context={'results': results,
                     'user': user_result}

            return render(request, 'search_fitur/search.html', context)

        else:
            return render(request, 'search_fitur/index.html')

    else:
        return render(request, 'search_fitur/index.html')


def searchposts2(request, kategori):

    query= kategori

    submitbutton= request.GET.get('submit')

    if query is not None:
        lookups= Q(kategori__icontains=query) 

        results= Post.objects.filter(lookups).distinct()
            

        context={'results': results}

        return render(request, 'search_fitur/category2.html', context)

    else:
        return render(request, 'search_fitur/index.html')
