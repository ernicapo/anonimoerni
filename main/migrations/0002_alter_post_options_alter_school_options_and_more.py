# Generated by Django 4.1.7 on 2023-07-18 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
        migrations.AlterModelOptions(
            name='userc',
            options={'verbose_name': 'PersonalizedUser', 'verbose_name_plural': 'PersonalizedUsers'},
        ),
    ]
