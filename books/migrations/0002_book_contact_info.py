# Generated by Django 2.2.5 on 2019-10-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contact_info',
            field=models.TextField(default='contact@info.com'),
            preserve_default=False,
        ),
    ]
