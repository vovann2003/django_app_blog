from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppBlogConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_blog'
    verbose_name = _('blog')
