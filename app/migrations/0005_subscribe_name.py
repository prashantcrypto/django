# Generated by Django 4.0.3 on 2022-11-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_empoly_emp_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
