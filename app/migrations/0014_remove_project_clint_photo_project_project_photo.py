# Generated by Django 4.0.3 on 2022-11-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_projects_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='clint_photo',
        ),
        migrations.AddField(
            model_name='project',
            name='project_photo',
            field=models.ImageField(default=None, null=True, upload_to='Project_img'),
        ),
    ]
