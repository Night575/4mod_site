# Generated by Django 4.2.3 on 2023-08-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_alter_advertisement_options_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
