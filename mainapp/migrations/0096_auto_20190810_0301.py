# Generated by Django 2.1.2 on 2019-08-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0095_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='hashtags',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='designation',
            field=models.CharField(max_length=250, verbose_name='Officer name'),
        ),
    ]
