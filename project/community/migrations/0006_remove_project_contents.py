# Generated by Django 3.1.3 on 2020-11-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contents',
        ),
    ]
