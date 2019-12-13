from .models import Post, User,Komen
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def index(request):
    blog=Post.objects.all()
    komen=Komen.objects.all()
    ctx={"blogs": blog, 'komen':komen}
    return render(request, 'search_fitur/index.html', ctx)
  
# ngarahin ke web baru detail
def coba(request, blog_id):
    blog=Post.objects.filter(pk=blog_id)
    komen=Komen.objects.filter(post_id=blog_id)
    ctx={'blog':blog, 'komen':komen}
    return render(request, 'search_fitur/detail.html', ctx )

# page baru nampilin kategori aja
def kategori(request):
    blog=Post.objects.all().distinct()
    return render(request, "search_fitur/category1.html", {"blogs":blog})
# all searchbar
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

# nampilin hasil filter dari page kategori
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
      
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'search_fitur/index.html', {'users': users})

def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            return redirect('login')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'register.html', {'u_form': u_form, 'p_form': p_form})
