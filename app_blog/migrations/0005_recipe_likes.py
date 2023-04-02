# Generated by Django 4.1.3 on 2023-02-19 12:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0004_recipecategory_name_en_recipecategory_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='recipe_likes', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
    ]