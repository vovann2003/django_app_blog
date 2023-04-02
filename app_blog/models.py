from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    """
    Модель Профиль пользователя
    """
    first_name = models.CharField(max_length=56, verbose_name=_('first name'))
    last_name = models.CharField(max_length=56, verbose_name=_('last_name'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'), unique=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name=_('user'))
    username = models.CharField(max_length=150, blank=True, null=True, verbose_name=_('username'), unique=True)
    photo = models.ImageField(upload_to='media/images/profile/', verbose_name=_('photo'), null=True, blank=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'profile'
        verbose_name_plural = _('profile')


class Recipe(models.Model):
    """
    Модель Рецепт
    """

    title = models.CharField(max_length=160, verbose_name=_('recipe title'))
    text = RichTextUploadingField(verbose_name=_('recipe text'), null=True, blank=True)
    heading = models.ForeignKey('RecipeCategory', verbose_name=_('heading'), on_delete=models.CASCADE)
    cooking_time = models.PositiveIntegerField(default=0, verbose_name=_('cooking time'))
    photo = models.ImageField(verbose_name=_('recipe photo'), upload_to='media/%Y/%m/%d')
    serving = models.PositiveIntegerField(default=0, verbose_name=_('serving'))
    published_at = models.DateField(auto_now_add=True, verbose_name=_('published at'))
    edited_at = models.DateField(auto_now=True, verbose_name=_('edited at'))
    views_count = models.PositiveIntegerField(default=0, verbose_name=_('views count'))
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name=_('slug'), default=None)
    is_published = models.BooleanField(default=True)
    ingredients = RichTextField(verbose_name=_('ingredients'))
    cooking_instructions = RichTextField(verbose_name=_('cooking instructions'))
    likes = models.ManyToManyField(User, related_name='recipe_likes', verbose_name=_('likes'))
    objects = models.Manager()

    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'recipe_slug': self.slug})

    class Meta:
        db_table = 'recipe'
        ordering = ('-published_at', )
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')


class RecipeCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name=_('category name'))
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recipe_category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class RecipeCountViews(models.Model):
    session_id = models.CharField(max_length=150, db_index=True)
    recipe_id = models.ForeignKey(Recipe, blank=True, null=True, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_id


class Comment(models.Model):
    """
    Класс Комментарий
    """
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length=1500, verbose_name=_('comment'))
    published_at = models.DateField(auto_now_add=True, verbose_name=_('published at'))
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True, null=True, related_name='comment_recipe')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comment'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
