# Generated by Django 4.1 on 2022-08-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_blog_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='blog-images/'),
        ),
    ]
