# Generated by Django 2.2.3 on 2020-04-01 00:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('picture', models.ImageField(blank=True, upload_to='meme_images')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('nsfw', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_id', models.CharField(max_length=64)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.Meme')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('dob', models.DateField()),
                ('bio', models.TextField(blank=True, default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meme',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.UserProfile'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.Meme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MemeRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.Meme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.UserProfile')),
            ],
            options={
                'unique_together': {('user', 'meme')},
            },
        ),
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meme_app.UserProfile')),
            ],
            options={
                'unique_together': {('user', 'comment')},
            },
        ),
    ]