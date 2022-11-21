# Generated by Django 4.0.3 on 2022-11-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('clint_photo', models.ImageField(default=None, null=True, upload_to='clint_img')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Web app', 'Web app'), ('Nfts', 'Nfts'), ('minting ui', 'Minting ui')], max_length=25)),
            ],
        ),
    ]
