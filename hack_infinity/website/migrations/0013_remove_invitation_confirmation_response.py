# Generated by Django 4.1.6 on 2023-02-04 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation_confirmation',
            name='Response',
        ),
    ]