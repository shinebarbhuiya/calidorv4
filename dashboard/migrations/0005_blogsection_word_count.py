# Generated by Django 4.1.2 on 2022-12-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_topic_blog_blogidea'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsection',
            name='word_count',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]