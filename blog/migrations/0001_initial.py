# Generated by Django 4.0.3 on 2022-11-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_post',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('Blog_title', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('author_image', models.ImageField(upload_to='')),
                ('blog_image', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
