# Generated by Django 3.0.6 on 2020-05-16 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200514_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postcode',
            new_name='postal_code',
        ),
    ]
