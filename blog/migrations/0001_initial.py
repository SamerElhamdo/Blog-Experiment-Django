# Generated by Django 2.2.2 on 2019-07-26 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=150)),
                ('bio', models.TextField()),
                ('job', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('personal_website', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tujruba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=999)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tujruba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tujruba')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tujruba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tujruba')),
            ],
        ),
    ]
