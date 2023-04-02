from django.urls import path
from django.views.decorators.cache import cache_page
from .views import ProfileFormView, Login, Logout, ProfileEditView, RecipeListView, RecipeDetailView, RecipeFormView, \
    ProfileView, PopularRecipe, like_view

urlpatterns = [
    path('register/', ProfileFormView.as_view(), name='register'),
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('recipe-list/<slug:slug>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe-form/', RecipeFormView.as_view(), name='recipe-form'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('recipe/popular/', PopularRecipe.as_view(), name='popular-recipe'),
    path('like/<slug:slug>', like_view, name='like'),
]
