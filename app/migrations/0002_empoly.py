# Generated by Django 4.0.3 on 2022-11-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empoly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_name', models.CharField(max_length=50)),
                ('Emp_design', models.CharField(max_length=30)),
                ('Emp_email', models.EmailField(max_length=254)),
                ('Emp_contact', models.IntegerField(max_length=10)),
            ],
        ),
    ]
