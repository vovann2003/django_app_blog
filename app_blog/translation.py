from modeltranslation.translator import TranslationOptions, register
from app_blog.models import Profile, Recipe, RecipeCountViews, Comment, RecipeCategory


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'ingredients', 'cooking_instructions')


@register(RecipeCategory)
class RecipeCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text', )
