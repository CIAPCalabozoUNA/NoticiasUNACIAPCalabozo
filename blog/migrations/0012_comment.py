# Generated by Django 5.0.4 on 2024-04-28 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_author_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=100)),
                ('ci', models.CharField(max_length=15)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
