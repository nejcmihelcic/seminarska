# Generated by Django 4.1.7 on 2023-04-03 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bounties', '0002_bounty_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bounty',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
