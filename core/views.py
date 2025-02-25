# core/views.py

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.core.paginator import Paginator
from .models import TeaGarden, News, Like, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, TeaGarden, TeaHistory, Tea
from .forms import ProfileForm
from django.http import JsonResponse

def home(request):
    # Fetch the tea gardens
    tea_gardens = TeaGarden.objects.all()[:5]

    # Fetch all news and paginate it
    news_list = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 5)  # Show 5 news articles per page
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    return render(request, 'index.html', {'tea_gardens': tea_gardens, 'news': news_page})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')  # Redirect to the homepage after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# View for a specific news article
# core/views.py

def news_detail(request, pk):
    news_article = get_object_or_404(News, pk=pk)  # Retrieve the news article based on the primary key (pk)
    likes_count = Like.objects.filter(news_article=news_article).count()  # Count the number of likes
    comments = Comment.objects.filter(news_article=news_article)  # Retrieve the comments related to this news article

    # Handle POST request for likes and comments
    if request.method == "POST" and request.user.is_authenticated:
        # Handle the "Like" action
        if "like" in request.POST:
            like, created = Like.objects.get_or_create(user=request.user, news_article=news_article)
            if not created:
                like.delete()  # If the like already exists, remove it (Unlike)
                messages.success(request, "You unliked this article.")
            else:
                messages.success(request, "You liked this article.")

        # Handle the "Comment" action
        elif "comment" in request.POST:
            comment_content = request.POST.get("comment")
            if comment_content.strip():  # Ensure the comment is not empty
                Comment.objects.create(user=request.user, news_article=news_article, content=comment_content)
                messages.success(request, "Your comment has been posted!")
            else:
                messages.error(request, "Comment cannot be empty.")  # Show error if the comment is empty

        return redirect('news_detail', pk=pk)  # Redirect to avoid form resubmission

    # Render the news detail page
    return render(request, 'news_detail.html', {
        'news_article': news_article,
        'likes_count': likes_count,
        'comments': comments
    })


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after update
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})

# Tea Gardens View
def tea_gardens(request):
    query = request.GET.get('q')
    if query:
        tea_gardens = TeaGarden.objects.filter(name__icontains=query)
    else:
        tea_gardens = TeaGarden.objects.all()
    return render(request, 'tea_gardens.html', {'tea_gardens': tea_gardens, 'query': query})


# Tea History View
def tea_history(request):
    tea_history = TeaHistory.objects.all()  # Get all tea history from the database
    return render(request, 'tea_history.html', {'tea_history': tea_history})

def tea_category(request):
    teas = Tea.objects.all()  # Retrieve all tea categories
    return render(request, 'tea_category.html', {'teas': teas})

def toggle_like(request, pk):
    news_article = get_object_or_404(News, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, news_article=news_article)

    if not created:
        like.delete()  # Unlike
        status = "unliked"
    else:
        status = "liked"  # Like the article

    likes_count = Like.objects.filter(news_article=news_article).count()
    return JsonResponse({"status": status, "likes_count": likes_count})

# Tea Category Detail View
def tea_detail(request, pk):
    tea = get_object_or_404(Tea, pk=pk)
    return render(request, 'tea_detail.html', {'tea': tea})

# Tea History Detail View
def tea_history_detail(request, pk):
    history = get_object_or_404(TeaHistory, pk=pk)
    return render(request, 'tea_history_detail.html', {'history': history})

# Tea Garden Detail View
def tea_garden_detail(request, pk):
    garden = get_object_or_404(TeaGarden, pk=pk)
    return render(request, 'tea_garden_detail.html', {'garden': garden})