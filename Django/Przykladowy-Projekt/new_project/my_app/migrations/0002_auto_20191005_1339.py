# Generated by Django 2.2.5 on 2019-10-05 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]