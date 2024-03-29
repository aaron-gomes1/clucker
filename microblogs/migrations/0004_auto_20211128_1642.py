# Generated by Django 3.2.7 on 2021-11-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0003_user_followers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=280),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=520),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
