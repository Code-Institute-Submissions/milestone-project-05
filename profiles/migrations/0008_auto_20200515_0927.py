# Generated by Django 3.0.6 on 2020-05-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200515_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designerprofile',
            name='register_designer',
        ),
        migrations.AddField(
            model_name='designerprofile',
            name='register_as_customer',
            field=models.BooleanField(blank=True, default='False'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designerprofile',
            name='register_as_designer',
            field=models.BooleanField(blank=True, default='False'),
            preserve_default=False,
        ),
    ]
