# Generated by Django 2.1.3 on 2018-12-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s7uploads', '0004_auto_20181223_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='img',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='url',
            field=models.CharField(default='none.png', max_length=100),
            preserve_default=False,
        ),
    ]