# Generated by Django 3.2.15 on 2022-09-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boundary',
            old_name='geom',
            new_name='mpoly',
        ),
        migrations.AlterField(
            model_name='boundary',
            name='pcode',
            field=models.CharField(max_length=1, verbose_name='Province Code'),
        ),
    ]
