# Generated by Django 4.1.3 on 2023-02-12 11:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_recipe_cooking_instructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='recipe text'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='recipe text'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='recipe text'),
        ),
    ]
