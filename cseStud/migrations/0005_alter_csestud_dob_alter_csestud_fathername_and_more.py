# Generated by Django 4.2.4 on 2023-08-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cseStud', '0004_remove_csestud_firstgraduate_remove_csestud_pending_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csestud',
            name='DOB',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='FatherName',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='FathersOccupation',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='Fees',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='Languages',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='MotherName',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='MothersOccupation',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='Place',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='Year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='YearOfJoin',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='registerNo',
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='csestud',
            name='rollno',
            field=models.CharField(blank=True, default=None, max_length=7, null=True),
        ),
    ]