# Generated by Django 4.1.2 on 2022-12-09 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_blog_audience_blog_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='topic',
            new_name='blogIdea',
        ),
    ]