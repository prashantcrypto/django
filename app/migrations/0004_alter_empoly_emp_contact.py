# Generated by Django 4.0.3 on 2022-11-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_empoly_emp_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empoly',
            name='Emp_contact',
            field=models.CharField(max_length=13),
        ),
    ]