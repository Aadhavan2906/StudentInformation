# Generated by Django 3.2.12 on 2023-07-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cseStud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csestud',
            name='rollno',
            field=models.CharField(max_length=7),
        ),
    ]