# Generated by Django 4.2.4 on 2023-09-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20151017_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='opt_out_entry_change_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='opt_out_entry_reminder_email',
            field=models.BooleanField(default=False),
        ),
    ]
