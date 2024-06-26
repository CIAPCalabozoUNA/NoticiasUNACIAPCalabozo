# Generated by Django 5.0.4 on 2024-04-28 14:50

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_article_created_at_article_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(upload_to='user_profile_upload/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='system_image_upload/'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(upload_to='document_upload/', validators=[blog.validators.validate_file_extension]),
        ),
    ]
