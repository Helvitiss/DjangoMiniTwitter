from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import  reverse
from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


from .forms import PostForm, CommentForm, SearchForm
from .models import Post, Comment

User = get_user_model()



class Index(TemplateView):
    template_name = "mainapp/index.html"

    def get(self, request, *args, **kwargs):
        """Обрабатывает GET-запрос: отображает посты и форму"""
        posts = Post.objects.all()
        form = PostForm()  # Форма для создания поста
        return render(request, self.template_name, {"posts": posts, "form": form})



    def post(self, request, *args, **kwargs):
        """Обрабатывает POST-запрос: создаёт новый пост"""
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Указываем автора
            post.save()
            return redirect("home")  # Перенаправляем на главную
        # Если форма невалидна, возвращаем ошибки
        posts = Post.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"posts": posts, "form": form})



@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Убираем лайк
        liked = False
    else:
        post.likes.add(request.user)  # Добавляем лайк
        liked = True

    return JsonResponse({"liked": liked, "likes_count": post.total_likes()})




class CommentView(DetailView, FormView):
    model = Post
    template_name = 'mainapp/comment.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('comment', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def form_valid(self, form):
        """Сохраняем комментарий и перенаправляем через GET-запрос"""
        form.instance.post = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return redirect(self.get_success_url())  # Перенаправляем, предотвращая дублирование



def search(request):
    form = SearchForm({})
    query = request.GET.get("query", "")
    results_posts = []
    results_users = []

    if query:
        results_posts = Post.objects.filter(content__icontains=query)  # Поиск по содержимому постов
        results_users = User.objects.filter(username__icontains=query)  # Поиск по пользователям
    print(request.GET)
    return render(request, "mainapp/search_results.html", {
        "form": form,
        "query": query,
        "results_posts": results_posts,
        "results_users": results_users
    })