from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea
from .models import Profile, Comment, Recipe
from django import forms
from django.utils.translation import gettext_lazy as _


class ProfileForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    first_name = forms.CharField(label='Имя', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'required': True,
                                                                                           'placeholder': _('Enter your Name')}))
    last_name = forms.CharField(label='Фамилия', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input', 
                                                                                              'required': True,
                                                                                              'placeholder': _('Enter your Surname')}))
    email = forms.EmailField(label='Электронная почта', required=False, widget=forms.EmailInput(attrs={'class': 'form-input', 
                                                                                                       'required': False,
                                                                                                       'placeholder': _('Enter your Email')}))
    username = forms.CharField(label='Логин', max_length=56, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                           'placeholder': _('Enter your Username')}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                  'placeholder': _('Enter your Password')}))
    password2 = forms.CharField(label='Повторение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                             'placeholder': _('Confirm your password')}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    """
    Форма для редактирования данных пользователя
    """

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'username')


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your Username')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Enter your Password')}))


class RecipeForm(forms.ModelForm):
    """
    Форма для добавления рецептов на сайт
    """

    class Meta:
        model = Recipe
        fields = ('title', 'title_ru', 'title_en', 'text', 'text_ru', 'text_en', 'heading', 'cooking_time', 'photo', 'serving', 'cooking_instructions', 'cooking_instructions_ru', 'cooking_instructions_en')


class CommentForm(forms.ModelForm):
    """
    Форма для комментариев
    """

    class Meta:
        model = Comment
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 3})
