from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, CreateView
from .models import Profile, Recipe, RecipeCategory
from .forms import ProfileForm, ProfileEditForm, CommentForm, RecipeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect


class GetCategories:

    def get_categories(self):
        return RecipeCategory.objects.all()


class ProfileFormView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, 'app_blog/profile/profile_form.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user_auth = authenticate(username=username, password=password)
            login(request, user_auth)
            return redirect('/')
        else:
            messages.error(request, 'Error')
        return render(request, 'app_blog/profile/profile_form.html', {'form': form})


class Login(LoginView):
    template_name = 'app_blog/profile/login.html'


class Logout(LogoutView):
    next_page = '/'


class ProfileView(View):

    def get(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        return render(request, 'app_blog/profile/profile.html', {'form': profile})


class ProfileEditView(UpdateView):
    """
    Обновление профиля пользователя
    """
    model = Profile
    queryset = Profile.objects.all()
    form_class = ProfileEditForm
    template_name = 'app_blog/profile/profile_edit.html'
    success_url = '/'


class RecipeFormView(CreateView):
    """
    Добавление рецептов на сайт
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'app_blog/recipe/recipe_form.html'


class RecipeListView(GetCategories, ListView):
    """
    Общий список рецептов
    """
    model = Recipe
    queryset = Recipe.objects.filter(is_published=True)
    template_name = 'app_blog/recipe/recipe_list.html'
    context_object_name = 'recipe_list'

    # def get(self, request):
    #     if cache.get('recipe'):
    #         queryset = cache.get('recipe')
    #         print("GETTING FROM CACHE")
    #     else:
    #         queryset = Recipe.objects.filter(is_published=True)
    #         cache.set('recipe', queryset)
    #         print('GETTING FROM DB')
    #     template_name = 'app_blog/recipe/recipe_list.html'
    #     context = {'recipe_list': queryset}
    #     return render(request, template_name, context)


def like_view(request, slug):
    liked = False
    recipe = get_object_or_404(Recipe, slug=request.POST.get('recipe_slug'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
    else:
        recipe.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('recipe-detail', args=[slug]))


class RecipeDetailView(FormMixin, DetailView):
    """
    Детальная информация рецепта
    """
    model = Recipe
    form_class = CommentForm
    queryset = Recipe.objects.all()
    template_name = 'app_blog/recipe/recipe_detail.html'
    context_object_name = 'recipe_detail'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        liked = False

        if self.object.likes.filter(id=request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['total_likes'] = self.object.get_total_likes()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.recipe = self.get_object()
        self.object.save()
        return super().form_valid(form)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RecipeDetailView, self).get_context_data(**kwargs)
    #     recipe_likes = get_object_or_404(Recipe, slug=[self.kwargs['slug']])
    #     total_likes = recipe_likes.get_total_likes()
    #     context['total_likes'] = total_likes

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('recipe-detail', kwargs={'recipe_slug': self.get_object().slug})


class PopularRecipe(ListView):
    """
    Самые просматриваемые рецепты
    """
    model = Recipe
    queryset = Recipe.objects.order_by('-views_count')[:5]
    template_name = 'app_blog/recipe/popular-recipe.html'
    context_object_name = 'recipe'

