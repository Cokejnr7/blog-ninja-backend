# Generated by Django 4.0.5 on 2022-11-16 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_categories_post_section_delete_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
