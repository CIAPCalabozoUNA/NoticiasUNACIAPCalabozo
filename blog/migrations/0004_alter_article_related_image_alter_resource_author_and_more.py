# Generated by Django 5.0.4 on 2024-04-27 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_related_image_alter_resource_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='related_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.image'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='related_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.image'),
        ),
    ]
